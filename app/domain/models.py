from typing import List

from pydantic import Field, BaseModel

class Document(BaseModel):
    title: str = Field(max_length=200)
    content: str = Field(max_length=2000)

class QueryResult(BaseModel):
    documents: List[Document]
