from typing import Any, Callable, TypeAlias

DecoratedFunc: TypeAlias = Callable[..., Any]


def retry(
    max_tries: int | DecoratedFunc = 3,
    exceptions: tuple[type[Exception], ...] | None = None,
    on_giveup: Callable[[Exception], None] | None = None,
) -> DecoratedFunc:
    # Catch all exception by default
    if exceptions is None:
        exceptions = (Exception,)

    decorated_func = None

    # If decorator was used without parentheses, then function is the first arg
    if callable(max_tries):
        decorated_func, max_tries = max_tries, 3

    def decorator(fn: DecoratedFunc) -> DecoratedFunc:
        def wrapper(*args, **kwargs) -> Any:
            for i in range(max_tries):
                try:
                    return fn(*args, **kwargs)
                except exceptions as exc:
                    if i + 1 == max_tries:
                        if on_giveup is None:
                            raise exc
                        return on_giveup(exc)

                    print(f"{fn.__name__} failed with {exc}, retrying")

        return wrapper

    # If decorated_func is already set, then run decoration immediately
    if decorated_func is not None:
        return decorator(decorated_func)

    return decorator


@retry
def to_celsius(fahrenheit: float) -> float:
    print(f"Calling to_celsius with {fahrenheit}")
    return (fahrenheit - 32) / 1.8


@retry(
    max_tries=2,
    exceptions=(TypeError,),
    on_giveup=lambda exc: print(f"Giving up: {exc}"),
)
def to_fahrenheit(celsius: float) -> float:
    print(f"Calling to_fahrenheit with {celsius}")
    return (celsius * 1.8) + 32


if __name__ == "__main__":
    to_celsius(100.0)
    to_fahrenheit(40)
    to_fahrenheit("50")
