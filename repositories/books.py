from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from models.book import Book
from schemas.book import SBookShow, SBookAdd, SBookPatch

class BookRepo:
    @classmethod
    async def get_books_paginator(cls, session: AsyncSession,
                                  limit: int | None = None,
                                  offset: int | None = None) -> list[SBookShow]:
        if limit and offset:
            query = select(Book).offset(offset).limit(limit)
        elif limit and not offset:
            query = select(Book).limit(limit)
        else:
            query = select(Book)

        books_scalar = await session.scalars(query)

        return [SBookShow.model_validate(book_orm, from_attributes=True)
                for book_orm in books_scalar.all()]


    @classmethod
    async def get_book_by_id(cls, session: AsyncSession, book_id: int) -> SBookShow | None:
        query = select(Book).where(Book.book_id == book_id)

        book_orm = await session.scalar(query)

        if book_orm:
            return SBookShow.model_validate(book_orm, from_attributes=True)


    @classmethod
    async def add_book(cls, session: AsyncSession, sch_book: SBookAdd) -> SBookShow:
        query = insert(Book).values(title=sch_book.title,
                     author=sch_book.author,
                     year=sch_book.year,
                     pages=sch_book.pages,
                     is_read=sch_book.is_read).returning(Book)

        book_orm = await session.scalar(query)

        await session.commit()

        return SBookShow.model_validate(book_orm, from_attributes=True)


    @classmethod
    async def patch_book(cls, session: AsyncSession, book_id: int, sch_book: SBookPatch) -> SBookShow | None:
        patch_items = {key: value for key, value in sch_book.model_dump().items()}

        query = (update(Book)
                 .values(**patch_items)
                 .where(Book.book_id == book_id)
                 .returning(Book))

        book_orm = await session.scalar(query)

        await session.commit()

        if book_orm:
            return SBookShow.model_validate(book_orm, from_attributes=True)


    @classmethod
    async def put_book(cls, session: AsyncSession, book_id: int, book_sch: SBookAdd) -> SBookShow | None:
        query = (update(Book)
                 .values(**book_sch.model_dump())
                 .where(Book.book_id == book_id))

        book_orm = await session.scalar(query)

        if book_orm:
            return SBookShow.model_validate(from_attributes=True)


    @classmethod
    async def delete_book_by_id(cls, session: AsyncSession, book_id: int) -> SBookShow | None:
        query = (delete(Book)
                 .where(Book.book_id == book_id)
                 .returning(Book))

        book_orm = await session.scalar(query)

        await session.commit()

        if book_orm:
            return SBookShow.model_validate(book_orm, from_attributes=True)









