from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import count
from starlette import status

from anekdot.backend.db import new_session
from anekdot.schemas import SAnekdotAdd, SAuthorAdd, SAuthor, SAnekdot
from anekdot.models import Author, Anekdot


class AuthorRepository:

    @classmethod
    async def add(cls, author_add: SAuthorAdd) -> SAuthor:
        async with new_session() as session:
            session: AsyncSession
            author = Author(**author_add.model_dump())
            session.add(author)
            await session.flush()
            await session.commit()
            return SAuthor.model_validate(author)

    @classmethod
    async def get_by(cls, **kwargs) -> SAuthor | None:
        async with new_session() as session:
            session: AsyncSession
            print(kwargs)
            if 'name' in kwargs:
                author = await session.scalar(
                    select(Author).where(Author.name == kwargs['name'])
                )
            elif 'id' in kwargs:
                author = await session.scalar(
                    select(Author).where(Author.id == kwargs['id'])
                )
            else:
                author = None
            return author


class AnekdotRepository:

    @classmethod
    async def get_by_id(cls, anekdot_id: int) -> SAnekdot | None:
        async with new_session() as session:
            session: AsyncSession
            anekdot = await session.scalar(
                select(Anekdot).where(Anekdot.id == anekdot_id)
            )
            return anekdot

    @classmethod
    async def add(cls, anekdot_add: SAnekdotAdd) -> SAnekdot:
        async with new_session() as session:
            session: AsyncSession

            if anekdot_add.author.name:
                author = await AuthorRepository.get_by(name=anekdot_add.author.name)
                if not author:
                    author = await AuthorRepository.add(SAuthorAdd(name=anekdot_add.author.name, link=anekdot_add.author.link))

            anekdot = Anekdot(text=anekdot_add.text, author_id=author.id)
            session.add(anekdot)
            await session.flush()
            await session.commit()
            anekdot = await session.scalar(
                select(Anekdot).where(Anekdot.id == anekdot.id)
            )

            return SAnekdot.model_validate(anekdot)


    @classmethod
    async def like(cls, anekdot_id):
        anekdot = await cls.get_by_id(anekdot_id)
        if not anekdot:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Anekdot with id {anekdot_id} not found!")
        anekdot.likes += 1
        async with new_session() as session:
            session: AsyncSession
            session.add(anekdot)
            await session.commit()
        return anekdot.likes

    @classmethod
    async def dislike(cls, anekdot_id):
        anekdot = await cls.get_by_id(anekdot_id)
        if not anekdot:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Anekdot with id {anekdot_id} not found!")
        anekdot.dislikes += 1
        async with new_session() as session:
            session: AsyncSession
            session.add(anekdot)
            await session.commit()
        return anekdot.dislikes


    @classmethod
    async def count(cls):
        async with new_session() as session:
            session: AsyncSession

            return await session.scalar(
                select(count()).select_from(Anekdot)
            )