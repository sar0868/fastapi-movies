from fastapi import (
    FastAPI,
    Request,
)


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
