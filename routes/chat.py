import os, httpx # pyright: ignore[reportMissingImports]
from fastapi import APIRouter, Request # pyright: ignore[reportMissingImports]

router = APIRouter()
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")

@router.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    if not N8N_WEBHOOK_URL:
        return {"reply": "Back-end sem N8N_WEBHOOK_URL configurado."}
    async with httpx.AsyncClient() as c:
        r = await c.post(N8N_WEBHOOK_URL, json=body, timeout=30)
        return {"status": r.status_code, "body": r.text}
