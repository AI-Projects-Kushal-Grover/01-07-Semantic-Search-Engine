import os
import logging
from typing import List, cast

from psycopg import sql
from psycopg.rows import class_row, AsyncRowFactory

from app.infrastructure.database import Database
from app.domain.entities import DocumentChunk

logger = logging.getLogger(__name__)

async_factory = cast(AsyncRowFactory, class_row(DocumentChunk))
database = Database(os.getenv("PG_CONNECTION_STRING", ""))

class DocumentChunkRepository():
    def __init__(self) -> None:
        self.table_name = "document_chunk"
        pass

    async def create_table_if_not_exists(self):
        query = self._compose_query("""
            CREATE TABLE IF NOT EXISTS {} (
                id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                title varchar(200),
                content varchar(2000),
                embedding vector(384)
            )
        """)
        try:
            logger.info("Creating table if not exists: %s", self.table_name)
            result = await database.execute(query)
            logger.info("Table ensured: %s", self.table_name)
            return result
        except Exception as ee:
            logger.exception("Failed to create or ensure table %s", self.table_name)
            raise

    async def insert(self, vector_store: DocumentChunk):
        query = self._compose_query("INSERT INTO {} (title, content, embedding) values (%s, %s, %s)")
        await database.execute(
            query,
            (self.table_name, vector_store.title, vector_store.content, vector_store.embedding)
        )

    async def select(self, embedding: List[float], limit = 5) -> List[DocumentChunk]:
        query = self._compose_query("SELECT * FROM {} ORDER BY embedding <-> %s LIMIT %s")
        results = await database.execute(
            query,
            (self.table_name, embedding, limit)
        )
        results.row_factory = async_factory
        return cast(list[DocumentChunk], await results.fetchall())

    def _compose_query(self, query) -> sql.Composed:
        return sql.SQL(query).format(sql.Identifier(self.table_name))