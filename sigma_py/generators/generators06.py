import pytest
from typing import Generator

from sigma_py.generators.utils import Database


@pytest.fixture
def db() -> Generator[Database, None, None]:
    db = Database()
    db.connect()
    yield db
    db._entries = []
    db.disconnect()


def test_add_entry(db: Database) -> None:
    assert db.entries == []
    db.add({"name": "Jon"})
    assert db.entries == [{"name": "Jon"}]
