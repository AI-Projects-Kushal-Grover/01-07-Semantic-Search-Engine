import os
import logging
from typing import List, cast

from psycopg import sql
from psycopg.rows import class_row, AsyncRowFactory

from app.infrastructure.database import Database
from app.domain.entities import VectorStore

logger = logging.getLogger(__name__)

async_factory = cast(AsyncRowFactory, class_row(VectorStore))
database = Database(os.getenv("PG_CONNECTION_STRING", ""))

class VectorStoreRepository():
    def __init__(self) -> None:
        self.table_name = "VectorStore"
        pass

    async def create_table_if_not_exists(self):
        query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS {} (
                id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                title varchar(200),
                content varchar(2000),
                embedding vector(384)
            )
        """).format(
            sql.Identifier(self.table_name)
        )
        try:
            logger.info("Creating table if not exists: %s", self.table_name)
            await database.execute(query)
            logger.info("Table ensured: %s", self.table_name)
        except Exception as ee:
            logger.exception("Failed to create or ensure table %s", self.table_name)
            raise

    async def insert(self, vector_store: VectorStore):
        await database.execute(
            "INSERT INTO %s (title, content, embedding) values (%s, %s, %s)",
            (self.table_name, vector_store.title, vector_store.content, vector_store.embedding)
        )

    async def select(self, embedding: List[float], limit = 5) -> List[VectorStore]:
        results = await database.execute(
            "SELECT * FROM %s ORDER BY embedding <-> %s LIMIT %s",
            (self.table_name, embedding, limit)
        )
        results.row_factory = async_factory
        return cast(list[VectorStore], await results.fetchall())
