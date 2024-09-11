from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

engine = create_async_engine("sqlite+aiosqlite:///base.db", echo=True)
new_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
