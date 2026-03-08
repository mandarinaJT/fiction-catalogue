from typing import List

import requests
from db.schemas import MediaDisplay, media_type
def search_ol(q:str):
    url = f"https://openlibrary.org/search.json?q={q}"
    response = requests.get(url)

    if response.status_code != 200:
        return{"error": "Failed to fetch data from Open Library"}
    
    data = response.json()
    docs = data.get("docs", [])

    results: List[MediaDisplay] = []
    for doc in docs:
        results.append(
            MediaDisplay(
        key=doc.get("key", ""),
        type=media_type.BOOK,
        title=doc.get("title", "Unknown"),
        authors=doc.get("author_name", []),
        year=doc.get("first_publish_year", 0),
        poster_url=f"https://covers.openlibrary.org/b/id/{doc.get('cover_i', 0)}-L.jpg"
    )
        )
    return results