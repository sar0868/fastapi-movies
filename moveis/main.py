from typing import Annotated

from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    status,
    Depends,
)

from schemas.movie import Movie

MOVIES = [
    Movie(
        movie_id=1,
        title="Побег из Шоушенка",
        description="""A banker convicted of uxoricide forms a 
friendship over a quarter century with a hardened convict, 
while maintaining his innocence and trying to remain hopeful 
through simple compassion.""",
    ),
    Movie(
        movie_id=2,
        title="Криминальное чтиво",
        description="""The lives of two mob hitmen, a boxer, a gangster and his wife, 
and a pair of diner bandits intertwine in four tales of 
violence and redemption.""",
    ),
    Movie(
        movie_id=3,
        title="Семь самураев",
        description="""Farmers from a village exploited by bandits hire a veteran samurai
for protection, and he gathers six other samurai to join him.
""",
    ),
]

app = FastAPI(
    title="Catalog movies",
)


@app.get("/")
def get_root(request: Request):
    docs_url = request.url.replace(
        path="/docs",
    )
    return {
        "message": "Catalog movies",
        "docs": str(docs_url),
    }


@app.get(
    "/movies",
    response_model=list[Movie],
)
def get_movies():
    return MOVIES


def prefetch_movie(
    movie_id: int,
) -> Movie:
    movie: Movie | None = next(
        (movie for movie in MOVIES if movie.movie_id == movie_id),
        None,
    )
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"movie with id={movie_id} not found",
    )


@app.get(
    "/movie",
    response_model=Movie,
)
def get_movie_by_id(
    movie: Annotated[Movie, Depends(prefetch_movie)],
):
    return movie
