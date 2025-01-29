from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import APIKeyHeader

from config import settings
from schemas import IMEICheckResponse
from utils import check_imei

api_router = APIRouter()
security = APIKeyHeader(name="Authorization")


async def authenticate(token: str = Depends(security)) -> bool:
    """Auth token check"""
    return token == settings.imeicheck_api_sandbox_token


@api_router.post("/check-imei", response_model=IMEICheckResponse)
async def check_imei_endpoint(imei: str, auth: bool = Depends(authenticate)):
    if not auth:
        raise HTTPException(status_code=403, detail="Invalid token")
    try:
        await check_imei(device_id=imei)
