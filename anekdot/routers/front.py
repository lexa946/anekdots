from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from anekdot.routers.main import random_anekdot


router = APIRouter(prefix="/anekdot", tags=['Front'])
templates = Jinja2Templates(directory="anekdot/templates")


@router.get('/')
async def index(request: Request):
    anekdots = []

    for _ in range(3):
        response = await random_anekdot()
        anekdots.append(response['anekdot'])
    print(anekdots)
    return templates.TemplateResponse("index.html", {
        "request": request, "anekdots": anekdots
    })