from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
)

from api.api_v1.movies.crud import MOVIES
from api.api_v1.movies.dependencies import prefetch_movie
from schemas.movie import Movie

router = APIRouter(
    tags=["Movies"],
)


@router.get(
    "/movies",
    response_model=list[Movie],
)
def get_movies():
    return MOVIES


@router.get(
    "/movie",
    response_model=Movie,
)
def get_movie_by_id(
    movie: Annotated[Movie, Depends(prefetch_movie)],
):
    return movie
