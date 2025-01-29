from typing import Optional

from pydantic import BaseModel, ConfigDict


class IMEICheckRequest(BaseModel):
    imei: str
    token: str


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
    repairCoverage: Optional[str] = None
    technicalSupport: Optional[str] = None
    modelDesc: Optional[str] = None
    demoUnit: Optional[bool] = None
    refurbished: Optional[bool] = None
    purchaseCountry: Optional[str] = None
    apple_region: Optional[str] = None
    fmiOn: Optional[bool] = None
    lostMode: Optional[str] = None
    usaBlockStatus: Optional[str] = None
    network: Optional[str] = None


class IMEICheckResponse(BaseModel):
    id: str
    type: str
    status: str
    orderId: str
    service: ServiceInfo
    amount: str
    deviceId: str
    processedAt: int
    properties: DeviceProperties

    model_config = ConfigDict(extra="allow")
