from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.routers.api import router as api_router
from app.routers.front import router as front_router


app = FastAPI()

app.include_router(api_router)
app.include_router(front_router)
app.mount('/static', StaticFiles(directory='app/static'), 'anekdot_static')
