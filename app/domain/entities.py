from typing import List

from pydantic import BaseModel

class DocumentChunk(BaseModel):    
    id: int | None = None
    title: str
    content: str
    embedding: List[float]
