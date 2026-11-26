import os, httpx # pyright: ignore[reportMissingImports]
from fastapi import APIRouter, Request # pyright: ignore[reportMissingImports]

router = APIRouter()
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")

# WhatsApp por outra conexão, não 【entity-Meta¦canonical_name=Meta】 - sem verificação hub.*
# Ela só manda POST com o JSON da mensagem
@router.post("/webhook/whatsapp")
async def webhook(request: Request):
    body = await request.json()
    print("WA", body)
    if N8N_WEBHOOK_URL:
        async with httpx.AsyncClient() as c:
            await c.post(N8N_WEBHOOK_URL, json=body, timeout=10)
    return {"ok": True}
