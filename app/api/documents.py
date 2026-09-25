from fastapi import APIRouter

from app.services.semantic_search import SementicSearch
from app.domain.models import Document

router = APIRouter()

sementic_search = SementicSearch()

@router.post("/index_document")
async def index_document(request: Document):
    return await sementic_search.index_document(request)
