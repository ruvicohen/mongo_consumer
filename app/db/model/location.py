from pydantic import BaseModel

class Location(BaseModel):
    region: str
    country: str
    city: str
    latitude: float
    longitude: float