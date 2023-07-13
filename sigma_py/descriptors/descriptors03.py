class PositiveInt:
    def __set_name__(self, owner: type, name: str):
        self.name = name

    def __set__(self, obj: object, value: int) -> None:
        if value <= 0:
            raise ValueError(f"Value of '{self.name}' must be a positive int")
        obj.__dict__[self.name] = value


class SomeClass:
    x = PositiveInt()
    y = PositiveInt()

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


some_object = SomeClass(1, 2)
print(some_object.x)
print(some_object.y)
