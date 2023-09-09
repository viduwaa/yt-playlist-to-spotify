import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from pytube import Playlist
from dotenv import load_dotenv

load_dotenv()

spotify_client_id = os.getenv("CLIENT_ID")
spotify_client_secret = os.getenv("CLIENT_SECRET")
spotify_redirect_uri = os.getenv("REDIRECT_URI")


scope = "playlist-modify-public"
username = "6h6dz1pffbn7wa61nztzwingt"

# auth of spotify

token = SpotifyOAuth(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri=spotify_redirect_uri,
    scope=scope,
    username=username,
)
spotifyObject = spotipy.Spotify(auth_manager=token)

# youtube playlistlink
user_playlist_link = input("Enter url for the youtube playlist:")
playlist1 = Playlist(user_playlist_link)


# add youtube playlist songs to a list
list_of_songs = []
for i in playlist1.videos:
    list_of_songs.append(i.title[0:30])


# create the spotify playlist
playlist_name = input("Enter a playlist name: ")
playlist_desc = input("Enter a playlist description: ")

spotifyObject.user_playlist_create(
    user=username, name=playlist_name, public=True, description=playlist_desc
)

# search in spotify and add songs to a list
spotify_songs = []

for j in list_of_songs:
    result = spotifyObject.search(j)
    spotify_songs.append(result["tracks"]["items"][0]["uri"])


# adding the songs to the spotify playlist that created
preplaylist = spotifyObject.user_playlists(user=username)
# f.write(json.dumps(preplaylist, sort_keys=4, indent=4))
playlist_identified = preplaylist["items"][0]["id"]

spotifyObject.user_playlist_add_tracks(
    user=username, playlist_id=playlist_identified, tracks=spotify_songs
)
