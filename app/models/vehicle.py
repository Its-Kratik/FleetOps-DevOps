from pydantic import BaseModel

class Vehicle(BaseModel):
    vehicle_id: str
    driver: str
    speed: int
    status: str