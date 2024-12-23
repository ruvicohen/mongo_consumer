from app.db.mongo_database import terror_events
from app.service.event_service import convert_to_mongo_compatible


def insert_events(event):
    event_dict = convert_to_mongo_compatible(event.dict())
    terror_events.insert_one(event_dict)
