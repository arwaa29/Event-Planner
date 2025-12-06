from bson import ObjectId

def attendee_helper(attendee, user) -> dict:

    return {
        "username": user["username"],
        "status": attendee.get("status", "pending")
    }