from pydantic import BaseModel

class Casualties(BaseModel):
    fatalities: int
    injuries: int