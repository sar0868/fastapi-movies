from fastapi import (
    FastAPI,
    Request,
)

from api import router as api_router

app = FastAPI(
    title="Catalog movies",
)

app.include_router(api_router)


@app.get("/")
def get_root(request: Request):
    docs_url = request.url.replace(
        path="/docs",
    )
    return {
        "message": "Catalog movies",
        "docs": str(docs_url),
    }
