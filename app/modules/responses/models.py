def response_helper(response) -> dict:
    attendees = response.get("attendees")
    attend = []
    for i in attendees:
        attend.append({ "user": i.get("user"),
        "status": i.get("status"),})

    return {
        "attendees": attend
    }