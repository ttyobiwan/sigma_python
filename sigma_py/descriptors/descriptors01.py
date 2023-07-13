class PositiveInt:
    def __init__(self, name: str) -> None:
        self.name = name

    def __set__(self, obj: object, value: int) -> None:
        if value <= 0:
            raise ValueError(f"Value of '{self.name}' must be a positive int")
        obj.__dict__[self.name] = value

    def __get__(self, obj: object, cls: type) -> int:
        return obj.__dict__[self.name]


class SomeClass:
    x = PositiveInt("x")
    y = PositiveInt("y")

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


some_object = SomeClass(1, 2)
print(some_object.x)
print(some_object.y)
some_object.y = 0
