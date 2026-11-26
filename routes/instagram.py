import os, httpx # pyright: ignore[reportMissingImports]
from fastapi import APIRouter, Request # pyright: ignore[reportMissingImports]
from fastapi.responses import PlainTextResponse # pyright: ignore[reportMissingImports]

router = APIRouter()
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "polcaronet-verify")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")

@router.get("/webhook/instagram")
async def verify(request: Request):
    params = request.query_params
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")
    mode = params.get("hub.mode")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge, status_code=200)
    return PlainTextResponse("forbidden", status_code=403)

@router.post("/webhook/instagram")
async def webhook(request: Request):
    body = await request.json()
    print("IG", body)
    if N8N_WEBHOOK_URL:
        async with httpx.AsyncClient() as c:
            await c.post(N8N_WEBHOOK_URL, json=body, timeout=10)
    return {"ok": True}
