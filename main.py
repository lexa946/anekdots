from fastapi import FastAPI
from anekdot.routers import main



app = FastAPI()

app.include_router(main.router)

