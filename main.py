from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from fastapi.middleware.cors import CORSMiddleware # pyright: ignore[reportMissingImports]
from routes import instagram, facebook, whatsapp, chat # pyright: ignore[reportMissingImports]

app = FastAPI(title="pol-back-end")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(instagram.router)
app.include_router(facebook.router)
app.include_router(whatsapp.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"ok": True, "service": "pol-back-end"}

@app.get("/api/health")
def health():
    return {"ok": True}
