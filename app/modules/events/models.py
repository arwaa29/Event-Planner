from bson import ObjectId

def event_helper(event, attendee_id: str = None, status: str = None) -> dict:
    event_data = {
        "id": str(event["_id"]),
        "title": event["title"],
        "date": (event["date"]),
        "time": (event["time"]),
        "location": event["location"],
        "description": event["description"],
        "organizer_id": event["organizer_id"]
    }

    if attendee_id:
        event_data["attendee_id"] = attendee_id
    if status:
        event_data["status"] = status
    return event_data


