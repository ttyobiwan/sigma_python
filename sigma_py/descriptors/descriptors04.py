import json
from typing import Any


class JSONAttribute:
    """A descriptor for working with JSON files."""

    def __set_name__(self, owner: type, name: str):
        self.name = name
        self.path = f"{owner.__name__}.json"

    def __set__(self, obj: object, value: Any) -> None:
        """Set the value in the JSON file."""
        try:
            f = open(self.path, "r+")
            content = json.load(f)
        except FileNotFoundError:
            f = open(self.path, "a+")
            content = {}

        content[self.name] = value
        f.seek(0)
        json.dump(content, f, indent=4)
        f.close()

    def __get__(self, obj: object, owner: type) -> Any:
        """Get the value from the JSON file."""
        try:
            f = open(self.path)
        except FileNotFoundError:
            f = open(self.path, "a+")
            json.dump({}, f)
            return None

        value = json.load(f).get(self.name)
        f.close()
        return value


class JSONReaderWriter:
    x = JSONAttribute()
    y = JSONAttribute()


rw = JSONReaderWriter()
rw.x = 1
rw.y = 2
print(rw.x, rw.y)
