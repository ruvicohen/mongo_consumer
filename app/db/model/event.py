from typing import List
from datetime import datetime
from app.db.model.casualities import Casualties
from app.db.model.location import Location


class Event:
    date: datetime
    location: Location
    groups_involved: List[str]
    attack_type: List[str]
    target_type: List[str]
    casualties: Casualties