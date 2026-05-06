from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from db.database import settings
from db.schemas import MediaDisplay, media_type
from typing import List

transport = RequestsHTTPTransport(
    url=settings.hardcover_api_url,
    headers={"Authorization": settings.hardcover_api_key},
    verify=True,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=False)

def search(q: str):
    query = gql("""
    query($q: String!) {
        search(query: $q) {
            hits {
                document {
                    id
                    title
                    author_names
                    release_year
                    image { url }
                }
            }
        }
    }
    """)

    result = client.execute(query, variable_values={"q": q})
    docs = result.get("search", {}).get("hits", [])

    results: List[MediaDisplay] = []

    for doc in docs:
        document = doc.get("document", {})

        results.append(
            MediaDisplay(
                key=document.get("id", ""),  # use "id" from document
                type=media_type.BOOK,
                title=document.get("title", "Unknown"),
                authors=document.get("author_names", []),
                year=document.get("release_year", 0),  # or another field like "first_publish_year" if available
                poster_url=document.get("image", {}).get("url", "")  # direct image URL
            )
        )
    
    return results