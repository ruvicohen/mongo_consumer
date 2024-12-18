from app.db.model.casualities import Casualties
from app.db.model.date import Date
from app.db.model.location import Location



def convert_to_mongo_compatible(data):
    if isinstance(data, Casualties):
        return {
            "fatalities": data.fatalities,
            "injuries": data.injuries
        }
    elif isinstance(data, Location):
        return {
            "region": data.region,
            "country": data.country,
            "city": data.city,
            "latitude": data.latitude,
            "longitude": data.longitude
        }
    elif isinstance(data, Date):
        return {
            "year": data.year,
            "month": data.month,
            "day": data.day
        }
    elif isinstance(data, dict):
        return data
    elif isinstance(data, list):
        return [convert_to_mongo_compatible(item) for item in data]
    else:
        return data
