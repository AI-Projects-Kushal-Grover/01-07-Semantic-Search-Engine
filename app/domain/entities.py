from typing import List

from pydantic import BaseModel

class DocumentChunk(BaseModel):    
    id: str
    title: str
    content: str
    embedding: List[float]
