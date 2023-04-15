from typing import Any, Callable


def register(func: Callable[..., Any]) -> Callable[..., Any]:
    results = []

    def wrapper(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        results.append(result)
        print(f"Results: {results}")
        return result

    return wrapper


@register
def to_fahrenheit(celsius: float) -> float:
    return (celsius * 1.8) + 32


if __name__ == "__main__":
    to_fahrenheit(10.0)
    to_fahrenheit(20.0)
    to_fahrenheit(30.0)

    for cell in to_fahrenheit.__closure__:  # type: ignore
        print(cell.cell_contents)
