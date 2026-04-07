from fastapi import APIRouter, HTTPException, status
from database import SessionDepend
from repositories.books import BookRepo
from schemas.book import SBookShow, SBookPatch, SBookAdd

router = APIRouter(prefix='/books', tags=['Books'])

@router.get('')
async def get_books(session: SessionDepend,
                    limit: int | None = None,
                    offset: int | None = None) -> list[SBookShow]:

    return await BookRepo.get_books_paginator(session, limit, offset)


@router.get('/{book_id}')
async def get_books(session: SessionDepend,
                    book_id: int) -> SBookShow:

    book = await BookRepo.get_book_by_id(session, book_id)

    if not book:
        raise HTTPException(status_code=404, detail='Книга не найдена')

    return book


@router.post('', status_code=status.HTTP_201_CREATED)
async def add_book(session: SessionDepend,
                   book: SBookAdd) -> SBookShow:

    return await BookRepo.add_book(session, book)


@router.patch('/{book_id}')
async def patch_book(session: SessionDepend,
                   book_id: int,
                   book: SBookPatch) -> SBookShow:

    book = await BookRepo.patch_book(session, book_id, book)

    if not book:
        raise HTTPException(status_code=404, detail='Книга не найдена')

    return book

@router.put('/{book_id}')
async def put_book(session: SessionDepend,
                   book_id: int,
                   book: SBookAdd) -> SBookShow:

    book = await BookRepo.put_book(session, book_id, book)

    if not book:
        raise HTTPException(status_code=404, detail='Книга не найдена')

    return book


@router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(session: SessionDepend, book_id: int):
    book = await BookRepo.delete_book_by_id(session, book_id)

    if not book:
        raise HTTPException(status_code=404, detail='Книга не найдена')




