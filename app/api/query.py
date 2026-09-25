from typing import Annotated

from fastapi import APIRouter, Query

from app.domain.models import QueryRequest
from app.services.semantic_search import SementicSearch

router = APIRouter()

sementic_search = SementicSearch()

@router.get("/query")
async def query(query: Annotated[QueryRequest, Query()]):
    return await sementic_search.search(query.search)
