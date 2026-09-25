from fastapi import APIRouter

from app.services.semantic_search import SementicSearch

router = APIRouter()

sementic_search = SementicSearch()

@router.get("/query")
async def query(search_query: str):
    return await sementic_search.search(search_query)
