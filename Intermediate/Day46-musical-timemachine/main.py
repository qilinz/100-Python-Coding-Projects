import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

# Spotify info
spotify_id = os.environ["SPOTIFY_ID"]
spotify_key = os.environ["SPOTIFY_KEY"]

# -------------------------STEP 1: get the date to travel to ---------------------------#
travel_date = input("Which date do you want to travel to? Type in the following format YYYY-MM-DD: ")


# ------------STEP 2: Get the top 100 music of the date through billboard --------------#
url = f"https://www.billboard.com/charts/hot-100/{travel_date}/"
response = requests.get(url)
response.raise_for_status()
music_data = response.text

# with open("billboard.txt", "w") as file:
#     file.write(response.text)
#
# with open("billboard.txt") as file:
#     music_data = file.read()

soup = BeautifulSoup(music_data, "html.parser")
# find the titles of music
titles = soup.select("li ul li h3")
# format the names
music_titles = [title.getText().replace("\n", "") for title in titles]


# ------------------------STEP 3: generate a playlist in Spotify ---------------------------#
# log in to Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_id,
        client_secret=spotify_key,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
year = travel_date.split("-")[0]
pp = pprint.PrettyPrinter(indent=4)

# get the url of all the songs
# Attention: it will only return the song of the given year.
# In the future, the artist of the song can be added for better search experience.
song_urls = []
for song in music_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        song_url = result["tracks"]["items"][0]["uri"]
        song_urls.append(song_url)
    except IndexError:
        print(f"{song} is not available in Spotify.")
# sp.current_user_saved_albums_add(albums=[])

# create the playlist
playlist_name = f"{travel_date} Billboard 100"
new_playlist = sp.user_playlist_create(user_id, playlist_name, public=False, collaborative=False, description='')
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(new_playlist)

playlist_id = new_playlist["id"]
playlist_link = new_playlist["external_urls"]["spotify"]

# add all the songs
sp.playlist_add_items(playlist_id, song_urls, position=None)

# print the link of the playlist for sharing
print(playlist_link)