from typing import Any, Callable, TypeAlias

DecoratedFunc: TypeAlias = Callable[..., Any]


def retry(max_tries: int = 3) -> DecoratedFunc:
    def decorator(fn: DecoratedFunc) -> DecoratedFunc:
        def wrapper(*args, **kwargs) -> Any:
            for i in range(max_tries):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:
                    if i + 1 == max_tries:
                        raise exc
                    print(f"{fn.__name__} failed with {exc}, retrying")

        return wrapper

    return decorator


@retry(max_tries=2)
def to_celsius(fahrenheit: float) -> float:
    print(f"Calling to_celsius with {fahrenheit}")
    return (fahrenheit - 32) / 1.8


if __name__ == "__main__":
    to_celsius(100.0)
    to_celsius(200.0)
    to_celsius("300")
