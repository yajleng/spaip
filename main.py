
from fastapi import FastAPI
from .api.routes import router as api_router

app = FastAPI(title="FastAPI on Render")
app.include_router(api_router)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
