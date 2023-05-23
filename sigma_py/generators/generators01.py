from typing import Generator


def calculate(a: int, b: int) -> Generator[int | float, None, None]:
    print(f"Starting calucations for {a} and {b}")

    print("Sum")
    yield a + b

    print("Subtraction")
    yield a - b

    print("Multiplication")
    yield a * b

    print("Division")
    yield a / b

    print("Done calculating")


calculations = calculate(10, 5)
for result in calculations:
    print("Result:", result)

calculations = calculate(10, 5)
print(next(calculations))
print(next(calculations))
print(next(calculations))
print(next(calculations))
# print(next(calculations))
