from pydantic import BaseModel
from typing import List

from app.db.model.casualities import Casualties
from app.db.model.date import Date
from app.db.model.location import Location


class Event(BaseModel):
    date: Date
    location: Location
    groups_involved: List[str]
    attack_type: List[str]
    target_type: List[str]
    casualties: Casualties
