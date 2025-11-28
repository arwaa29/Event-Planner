from bson import ObjectId

def attendee_helper(attendee) -> dict:

    return {
        "user_id": str(attendee["user_id"]),
        "status": attendee.get("status", "pending")
    }