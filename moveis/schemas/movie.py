from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_id: int
    title: str
    description: str


class Movie(MovieBase):
    """
    Модель записи фильма в каталоге
    """
