def search_helper(search) -> dict:
    return {
        "title": search["title"],
        "date": search["date"],
        "description": search["description"],
        "attendees": [i["role"] for i in search["attendees"]],
    }