class NegativeInt:
    def __init__(self, name: str) -> None:
        self.name = name

    def __set__(self, obj: object, value: int) -> None:
        if value >= 0:
            raise ValueError(f"Value of '{self.name}' must be a negative int")
        self.__dict__[self.name] = value

    def __get__(self, obj: object, cls: type) -> int:
        return self.__dict__[self.name]


class DifferentClass:
    x = NegativeInt("x")


some_object = DifferentClass()
some_object.x = -5
print(some_object.x)

different_object = DifferentClass()
different_object.x = -6
print(different_object.x)

print(some_object.x)
