from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"

SPOTIPY_CLIENT_ID = "dd74573e704545a4b4925c91a14394f2"
SPOTIPY_CLIENT_SECRET = "5bcaa22889a5433eb0da7d225c48b54e"
SPOTIPY_REDIRECT_URI = "https://www.example.com"
SCOPE = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=SCOPE,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    show_dialog=True,
    cache_path="token.txt"
    ))

user_id = sp.current_user()["id"]


date = input("Which year do you want to travel do? Type the date in this format YYYY-MM-DD:")

response = requests.get(URL + "1992-05-30").text

soup = BeautifulSoup(response, "html.parser")

"""list_songs = soup.find_all(name="h3", class_="u-letter-spacing-0021")
list_songs_titles = [title.getText().strip() for title in list_songs]
print(list_songs_titles)"""

songs = soup.select(selector="li > h3")

song_titles = [song.getText().strip() for song in songs[:100]]


list_uri = []
year = date.split("-")[0]

for song in song_titles:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        list_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.")


sp_playlist = spotipy.Spotify(auth_manager= SpotifyOAuth(
    scope="playlist-modify-private",
    client_id= SPOTIPY_CLIENT_ID,
    client_secret= SPOTIPY_CLIENT_SECRET,
    redirect_uri= SPOTIPY_REDIRECT_URI,
    show_dialog=True,
    cache_path="playlist.txt"
    ))

cs = sp_playlist.current_user()["id"]

playlist_id = sp_playlist.current_user_playlists()["items"][0]["id"]

# sp_playlist.user_playlist_create(user=cs, name=f"{date} Billboard 100", public=False)

sp_playlist.playlist_add_items(playlist_id= playlist_id, items= list_uri)
