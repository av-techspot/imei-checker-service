from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class IMEICheckCreateRequest(BaseModel):
    device_id: str = Field(..., alias="deviceId", min_length=15, max_length=15)
    service_id: int = Field(..., alias="serviceId", ge=1)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "deviceId": "356735111052198",
                "serviceId": 1
            }
        }
    )


class ServiceInfo(BaseModel):
    id: int
    title: str


class DeviceProperties(BaseModel):
    deviceName: Optional[str] = None
    image: Optional[str] = None
    imei: str
    estPurchaseDate: Optional[int] = None
    simLock: Optional[bool] = None
    warrantyStatus: Optional[str] = None
    modelDesc: Optional[str] = None
    demoUnit: Optional[bool] = None
    refurbished: Optional[bool] = None
    purchaseCountry: Optional[str] = None
    apple_region: Optional[str] = None
    fmiOn: Optional[bool] = None
    usaBlockStatus: Optional[str] = None
    network: Optional[str] = None


class IMEICheckResponse(BaseModel):
    id: str
    type: str
    status: str
    orderId: Optional[str] = None
    service: ServiceInfo
    amount: str
    deviceId: str
    processedAt: int
    properties: DeviceProperties

    model_config = ConfigDict(extra="allow")
