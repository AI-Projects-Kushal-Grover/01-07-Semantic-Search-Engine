from app.domain.models import Document, QueryResult
from app.repositories.document_chunk import DocumentChunkRepository

class SementicSearch():
    def __init__(self) -> None:
        self.document_chunk_repository = DocumentChunkRepository()

    async def index_document(self, document: Document):
        pass

    async def search(self, query: str) -> QueryResult:
        query_result = QueryResult(documents=[])
        return query_result
