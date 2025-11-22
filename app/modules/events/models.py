def event_helper(event) -> dict:
    return {
        "id": str(event["_id"]),
        "title": event["title"],
        "date": event["date"],
        "time": event["time"],
        "location": event["location"],
        "description": event["description"],
        "organizer": event["organizer"],
        "attendees": event["attendees"],
    }