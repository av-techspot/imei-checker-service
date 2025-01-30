from fastapi import APIRouter, Depends, HTTPException, Header

from api.schemas import IMEICheckResponse, IMEICheckCreateRequest
from api.utils import check_imei
from config import settings

api_router = APIRouter()


async def authenticate(token: str = Header(...)) -> bool:
    """Auth token check"""
    return token == settings.IMEICHECK_API_SANDBOX_TOKEN


@api_router.post("/check-imei", response_model=IMEICheckResponse)
async def check_imei_endpoint(body: IMEICheckCreateRequest, auth: bool = Depends(authenticate)):
    if not auth:
        raise HTTPException(status_code=403, detail="Invalid token")
    try:
        return await check_imei(
            device_id=body.device_id,
            service_id=body.service_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
