from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from anekdot.routers import main, front



app = FastAPI()

app.include_router(main.router)
app.include_router(front.router)
app.mount('/anekdot/static/', StaticFiles(directory='anekdot/static'), 'anekdot_static')
