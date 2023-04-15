from functools import lru_cache


@lru_cache(maxsize=2)
def to_fahrenheit(celsius: float) -> float:
    print(f"Calling to_fahrenheit with {celsius}")
    return (celsius * 1.8) + 32


if __name__ == "__main__":
    to_fahrenheit(10.0)
    to_fahrenheit(20.0)
    to_fahrenheit(20.0)
    to_fahrenheit(30.0)
    to_fahrenheit(40.0)
    to_fahrenheit(20.0)
