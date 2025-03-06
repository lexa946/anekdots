from pydantic import BaseModel, ConfigDict, Field


class SAuthorAdd(BaseModel):
    name: str = Field(examples=["Алексей"])
    link: str | None = Field(examples=["https://t.me/PozharAlex"])

    model_config = ConfigDict(from_attributes=True)


class SAuthor(SAuthorAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SAnekdotAdd(BaseModel):
    text: str = Field(examples=["Колобок повесился!"])
    author: SAuthorAdd | None = None

    model_config = ConfigDict(from_attributes=True)


class SAnekdot(SAnekdotAdd):
    id: int
    likes: int = 0
    dislikes: int = 0

    model_config = ConfigDict(from_attributes=True)