from typing import Generator
from fastapi import FastAPI, APIRouter, Depends

from sigma_py.generators.utils import Database

app = FastAPI()
router = APIRouter()


def get_db() -> Generator[Database, None, None]:
    db = Database()
    db.connect()
    yield db
    db.disconnect()


@router.get("/entries")
async def get_entries(db: Database = Depends(get_db)) -> list[dict]:
    return db.entries
