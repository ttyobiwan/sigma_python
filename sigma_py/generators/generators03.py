from typing import Generator


large_numbers_dataset = list(range(1, 11))
print(large_numbers_dataset)


def square_even(numbers: list[int]) -> Generator[int, None, None]:
    for n in numbers:
        if n % 2 == 0:
            yield n**2


squared = square_even(large_numbers_dataset)
print(squared)
print(list(squared))

squared_exp = (n**2 for n in large_numbers_dataset if n % 2 == 0)
print(squared_exp)
print(list(squared_exp))

print(sum(n**2 for n in large_numbers_dataset if n % 2 == 0))
