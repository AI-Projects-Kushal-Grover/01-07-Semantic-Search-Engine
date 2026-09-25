from typing import List

from pydantic import Field, BaseModel

class Document(BaseModel):
    title: str = Field(max_length=200)
    content: str = Field()

class QueryResult(BaseModel):
    documents: List[Document]
