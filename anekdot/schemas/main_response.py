from pydantic import BaseModel
from .main import SAnekdot


class SAnekdotResponse(BaseModel):
    status_code: int
    anekdot: SAnekdot