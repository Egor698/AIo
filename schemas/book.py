from pydantic import BaseModel, Field

class SBookBase(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    is_read: bool

class SBookShow(SBookBase):
    book_id: int

class SBookAdd(SBookBase):
    pass

class SBookPatch(SBookBase):
    title: str | None = None
    author: str | None = None
    year: int | None = None
    pages: int | None = None
    is_read: bool | None = None
