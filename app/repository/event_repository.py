from app.db.mongo_database import terror_events


def save_to_mongo(events):
    documents = [event.__dict__ for event in events]
    terror_events.insert_many(documents)
    print(f"{len(events)} events saved to MongoDB.")