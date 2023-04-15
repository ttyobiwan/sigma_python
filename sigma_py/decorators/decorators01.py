from typing import Any, Callable
import functools


def announcer(func: Callable[..., Any]) -> Callable[..., Any]:
    print(f"Decorating {func.__name__}")

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"The result is {result}")
        return result

    return wrapper


@announcer
def to_fahrenheit(celsius: float) -> float:
    return (celsius * 1.8) + 32


def to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) / 1.8


to_celsius = announcer(to_celsius)


if __name__ == "__main__":
    print(to_fahrenheit)
    print(to_fahrenheit.__annotations__)
    print(to_celsius)
    print(to_celsius.__annotations__)
