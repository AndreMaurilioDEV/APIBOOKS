from app import db
from sqlalchemy.orm import Mapped, mapped_column

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    genre: Mapped[str]
    year: Mapped[int]
    title: Mapped[str]


def to_dict(self):
    return {
        "id": self.id,
        "title": self.author,
        "author": self.genre,
        "year": self.year,
        "genre": self.title
    }
