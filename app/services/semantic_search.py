from app.domain.models import Document, QueryResult
from app.repositories.vector_store import VectorStoreRepository

class SementicSearch():
    async def index_document(self, document: Document):
        pass

    async def search(self, query: str) -> QueryResult:
        query_result = QueryResult(documents=[])
        return query_result
