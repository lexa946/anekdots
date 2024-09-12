from fastapi import APIRouter, Path, HTTPException
from starlette import status
from typing_extensions import Annotated

from anekdot.schemas import SAnekdotAdd, SAuthorAdd
from anekdot.schemas.main_response import SAnekdotResponse, SAuthorResponse
from anekdot.backend.repository import AnekdotRepository, AuthorRepository

router = APIRouter(prefix="/anekdot/api/anekdot", tags=['Anekdot'])


@router.post('/author')
async def add_author(author_add: SAuthorAdd) -> SAuthorResponse:
    author = await AuthorRepository.add(author_add)
    return {
        'status_code': status.HTTP_201_CREATED,
        'author': author
    }


@router.get('/random')
async def random_anekdot() -> SAnekdotResponse:

    anekdot = await AnekdotRepository.get_random()

    return {
        'status_code': status.HTTP_200_OK,
        'anekdot': anekdot
    }


@router.get('/{anekdot_id}')
async def get_anekdot_by_id(anekdot_id: Annotated[int, Path(ge=1)]) -> SAnekdotResponse:
    anekdot = await AnekdotRepository.get_by_id(anekdot_id)
    if anekdot:
        return {
            'status_code': status.HTTP_200_OK,
            'anekdot': anekdot
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Anekdot with id {anekdot_id} not found!'
        )


@router.post('/')
async def add_anekdot(anekdot_add: SAnekdotAdd) -> SAnekdotResponse:
    anekdot = await AnekdotRepository.add(anekdot_add)
    return {
        'status_code': status.HTTP_201_CREATED,
        'anekdot': anekdot
    }


@router.post('/like/{anekdot_id}')
async def like(anekdot_id: int) -> dict[str, int]:
    likes = await AnekdotRepository.like(anekdot_id)
    return {
        'status_code': status.HTTP_200_OK,
        'likes': likes
    }


@router.post('/dislike/{anekdot_id}')
async def like(anekdot_id: int) -> dict[str, int]:
    dislikes = await AnekdotRepository.dislike(anekdot_id)
    return {
        'status_code': status.HTTP_200_OK,
        'dislikes': dislikes
    }

