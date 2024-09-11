from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.util import await_only

from anekdot.backend.db import Base

class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    link: Mapped[str] = mapped_column(String(100))
    anekdots = relationship("Anekdot", back_populates="author")





class Anekdot(Base):
    __tablename__ = 'anekdots'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    text: Mapped[str] = mapped_column(String(300))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=True)
    author = relationship(Author, back_populates="anekdots", lazy="joined")
    likes: Mapped[int] = mapped_column(default=0)
    dislikes: Mapped[int] = mapped_column(default=0)



