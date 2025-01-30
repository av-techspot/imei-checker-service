import httpx

from api.schemas import IMEICheckResponse
from config import settings


async def check_imei(device_id: str, service_id: int = 12) -> IMEICheckResponse:
    url = "https://api.imeicheck.net/v1/checks"
    headers = {
        "Authorization": f"Bearer {settings.IMEICHECK_API_SANDBOX_TOKEN}",
        "Accept-Language": "en",
        "Content-Type": "application/json",
    }
    payload = {
        "deviceId": device_id,
        "serviceId": service_id,
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url=url, json=payload, headers=headers)
            response.raise_for_status()
            return IMEICheckResponse.model_validate(response.json())
        except httpx.HTTPStatusError as e:
            error_details = f"Cannot proccess the request: {e.response.status_code} - {e.response.text}"

            raise ValueError(error_details)
        except Exception as e:
            print(str(e))
            raise ValueError(f"IMEI check error: {str(e)}")
