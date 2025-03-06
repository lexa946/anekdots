from pydantic import BaseModel
from .main import SAnekdot, SAuthor


class SAnekdotResponse(BaseModel):
    status_code: int
    anekdot: SAnekdot

class SAuthorResponse(BaseModel):
    status_code: int
    author: SAuthor
