from typing import Any, Callable, TypeAlias

DecoratedFunc: TypeAlias = Callable[..., Any]


class Retry:
    def __init__(self, max_tries: int = 3) -> None:
        self.max_tries = max_tries

    def __call__(self, fn: DecoratedFunc) -> DecoratedFunc:
        def wrapper(*args, **kwargs) -> Any:
            for i in range(self.max_tries):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:
                    if i + 1 == self.max_tries:
                        raise exc
                    print(f"{fn.__name__} failed with {exc}, retrying")

        return wrapper


retry = Retry


@retry(max_tries=2)
def to_celsius(fahrenheit: float) -> float:
    print(f"Calling to_celsius with {fahrenheit}")
    return (fahrenheit - 32) / 1.8


if __name__ == "__main__":
    to_celsius(100.0)
    to_celsius(200.0)
    to_celsius("300")
