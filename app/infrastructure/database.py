import logging
import psycopg
from pgvector.psycopg import register_vector_async
from psycopg.abc import Params, QueryNoTemplate

logger = logging.getLogger(__name__)

class Database:
    def __init__(self, connection_string: str) -> None:
        self.connection: psycopg.AsyncConnection | None = None
        self.connection_string = connection_string
        logger.debug("Database initialized with connection_string: %s", "***hidden***" if connection_string else "(empty)")

    async def _connect(self, connection_string: str):
        logger.info("Connecting to database")
        try:
            conn = await psycopg.AsyncConnection.connect(connection_string)
            try:
                conn.autocommit = True
            except Exception as ee:
                logger.debug("Could not set autocommit on connection, continuing")
            await register_vector_async(conn)
            self.connection = conn
            logger.info("Database connection established")
            return conn
        except Exception as e:
            logger.exception("Failed to connect to database: %s", e)
            raise

    async def execute(self, query: QueryNoTemplate, params: Params | None = None):
        if (self.connection is None):
            self.connection = await self._connect(self.connection_string)
        try:
            logger.debug("Executing query: %s; params: %s", query, params)
            result = await self.connection.execute(query, params)
            await result.connection.commit()
            logger.debug("Query executed")
            return result
        except Exception as e:
            logger.exception("Query execution failed: %s", e)
            raise
    