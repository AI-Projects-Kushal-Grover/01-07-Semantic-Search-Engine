from app.domain.entities import DocumentChunk
from app.domain.models import Document, QueryResult
from app.repositories.document_chunk import DocumentChunkRepository
from app.services.chunker import Chunker
from app.services.embedder import Embedder

class SementicSearch():
    def __init__(self) -> None:
        self.document_chunk_repository = DocumentChunkRepository()
        self.embedder = Embedder()

    async def index_document(self, document: Document):
        chunks = Chunker.chunk_fixed_size(document.content, document.chunk_size, document.chunk_overlap)
        embeddings = self.embedder.embed(chunks)
        for index, embedding in enumerate(embeddings):
            await self.document_chunk_repository.insert(DocumentChunk(
                title=document.title,
                content=chunks[index],
                embedding=embedding
            ))

    async def search(self, query: str) -> QueryResult:
        query_result = QueryResult(documents=[])
        return query_result
