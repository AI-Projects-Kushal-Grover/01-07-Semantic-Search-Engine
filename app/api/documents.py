from fastapi import APIRouter

from app.services.semantic_search import SemanticSearch
from app.domain.models import Document

router = APIRouter()

semantic_search = SemanticSearch()

@router.post("/index_document")
async def index_document(request: Document):
    return await semantic_search.index_document(request)
