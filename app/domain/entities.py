from typing import List
from dataclasses import dataclass

from pydantic import BaseModel

@dataclass
class VectorStore(BaseModel):    
    id: str
    title: str
    content: str
    embedding: List[float]
