import requests

BASE_URL = "https://musicbrainz.org/ws/2"

def search_artist(query):
    response = requests.get(f"{BASE_URL}/artist/", params={"query": query, "fmt": "json"})
    response.raise_for_status()
    return response.json()["artists"]

def get_albums_by_artist(artist_id):
    response = requests.get(f"{BASE_URL}/release-group/", params={"artist": artist_id, "type": "album", "fmt": "json"})
    response.raise_for_status()
    return response.json()["release-groups"]