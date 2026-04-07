from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import Depends

engine = create_async_engine('sqlite+aiosqlite:///library.db')

session_factory = async_sessionmaker(engine)

async def get_db():
    async with session_factory(expire_on_commit=False) as session:
        yield session


SessionDepend = Annotated[AsyncSession, Depends(get_db)]