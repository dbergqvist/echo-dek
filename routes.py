from flask import request, jsonify
from musicbrainz_client import search_artist, get_albums_by_artist
from spotify_client import generate_spotify_uri
from apple_music_client import generate_apple_music_uri

def init_routes(app):
    @app.route("/search_artist", methods=["GET"])
    def search_artist_route():
        query = request.args.get("query")
        if not query:
            return jsonify({"error": "Query parameter is required"}), 400
        artists = search_artist(query)
        return jsonify(artists)

    @app.route("/artist/<artist_id>/albums", methods=["GET"])
    def get_albums_route(artist_id):
        albums = get_albums_by_artist(artist_id)
        return jsonify(albums)

    @app.route("/album/<album_id>/uris", methods=["GET"])
    def get_album_uris_route(album_id):
        spotify_uri = generate_spotify_uri(album_id)
        apple_music_uri = generate_apple_music_uri(album_id)
        return jsonify({"spotify_uri": spotify_uri, "apple_music_uri": apple_music_uri})