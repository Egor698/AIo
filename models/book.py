import asyncio
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from database import engine

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'books'

    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int]
    pages: Mapped[int]
    is_read: Mapped[bool]


async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(init())