class Database:
    def __init__(self) -> None:
        self._entries: list[dict] = []
        self._connected = False

    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

    def add(self, entry: dict) -> None:
        if self._connected is False:
            raise ConnectionError("Database is disconnected")
        self._entries.append(entry)

    @property
    def entries(self) -> list[dict]:
        if self._connected is False:
            raise ConnectionError("Database is disconnected")
        return self._entries
