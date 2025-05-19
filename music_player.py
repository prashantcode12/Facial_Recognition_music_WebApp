import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
import pygame

# 🔹 Replace these with your actual Spotify credentials
SPOTIPY_CLIENT_ID = "943f5f5c43f340fd990664b814e0470c"
SPOTIPY_CLIENT_SECRET = "1fd3a5eabdd844538570c38f191228d4"

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

# Initialize Pygame for stopping music
pygame.mixer.init()

# 🎭 Emotion-based Spotify search URLs
SPOTIFY_SEARCH_URLS = {
    "Happy": "https://open.spotify.com/search/happy%20hindi%20songs",
    "Sad": "https://open.spotify.com/search/sad%20song",
    "Angry": "https://open.spotify.com/search/angry%20songs",  # ✅ Now includes "Angry Songs"
    "Neutral": "https://open.spotify.com/search/koi%20itna%20khoobsurat"
}

def play_music(emotion):
    """Plays music by opening a Spotify search page for the detected emotion."""
    stop_music()  # ✅ Stop any currently playing music before starting a new one

    if emotion not in SPOTIFY_SEARCH_URLS:
        print(f"Error: No music found for emotion '{emotion}'")
        return

    try:
        # Open Spotify search page for the detected emotion
        webbrowser.open(SPOTIFY_SEARCH_URLS[emotion])
        print(f"Opened Spotify search for {emotion}: {SPOTIFY_SEARCH_URLS[emotion]}")

    except Exception as e:
        print(f"Error opening Spotify: {e}")

def stop_music():
    """Stops any playing local music using Pygame."""
    pygame.mixer.music.stop()
    print("Music Stopped")
