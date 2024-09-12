from fastapi import APIRouter, Request, Form, Path
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status
from typing_extensions import Annotated

from anekdot.routers.main import random_anekdot, add_anekdot, get_anekdot_by_id
from anekdot.schemas import SAnekdotAdd, SAuthorAdd

router = APIRouter(prefix="/anekdot", tags=['Front'])
templates = Jinja2Templates(directory="anekdot/templates")


@router.get('/')
async def index(request: Request):
    anekdots = []

    for _ in range(3):
        response = await random_anekdot()
        anekdots.append(response['anekdot'])
    return templates.TemplateResponse("index.html", {
        "request": request, "anekdots": anekdots
    })


@router.get('/add')
async def add_get(request: Request):
    return templates.TemplateResponse("add.html", {
        "request": request
    })


@router.post('/add')
async def add_post(request: Request, anekdot_text: Annotated[str, Form()],
                   author_name: Annotated[str, Form(max_length=50)],
                   author_link: Annotated[str, Form(max_length=100)]):
    author_add = SAuthorAdd(name=author_name, link=author_link)
    anekdot_add = SAnekdotAdd(text=anekdot_text, author=author_add)
    response = await add_anekdot(anekdot_add)
    return RedirectResponse(f"http://127.0.0.1:8082/anekdot/{response['anekdot'].id}", status_code=status.HTTP_302_FOUND)

@router.get('/{anekdot_id:int}')
async def get_by_id(request: Request, anekdot_id: Annotated[int, Path(ge=1)]):
    response = await get_anekdot_by_id(anekdot_id)
    return templates.TemplateResponse("one.html", {
        "request": request, "anekdot": response['anekdot'],
    })

