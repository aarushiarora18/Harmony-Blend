import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='b1e8646a7fda43cb8467c16d1a2940a1',
                                               client_secret='d5e60893f7c340158fee35fe4e67beb5',
                                               redirect_uri='http://localhost:8889/callback',
                                               scope='playlist-read-private playlist-modify-public playlist-modify-private'))

st.title('Harmony Blend')
user_playlist_id = st.text_input('Enter your Spotify playlist ID:')

# Function to get audio features of a track
def get_audio_features(track_id):
    features = sp.audio_features(track_id)[0]
    return [
        features['danceability'], features['energy'], features['key'], features['loudness'],
        features['mode'], features['speechiness'], features['acousticness'], features['instrumentalness'],
        features['liveness'], features['valence'], features['tempo'], features['duration_ms'],
        features['time_signature']
    ]

# Function to convert genre list into a vector
def genre_vector(genres, all_genres):
    return [1 if genre in genres else 0 for genre in all_genres]

# Fetch user playlist and recommended songs
if user_playlist_id:
    st.write(f"Fetching songs from playlist ID: {user_playlist_id}")
    
    try:
        # Get user playlist tracks
        user_playlist_tracks = sp.playlist_tracks(user_playlist_id)
        
        if not user_playlist_tracks['items']:
            st.error("No tracks found in the playlist. Please check the playlist ID.")
        else:
            # Collect user songs and features
            user_songs = []
            all_genres = set()
            for track in user_playlist_tracks['items']:
                song_name = track['track']['name']
                artist_name = track['track']['artists'][0]['name']
                artist_id = track['track']['artists'][0]['id']
                track_id = track['track']['id']
                genres = sp.artist(artist_id)['genres']  # Get the artist's genres
                all_genres.update(genres)  # Collect all genres
                
                # Get audio features
                audio_features = get_audio_features(track_id)
                
                # Append song with features and metadata
                user_songs.append({
                    'name': song_name,
                    'artist': artist_name,
                    'features': audio_features,
                    'genres': genres
                })

            # Display user playlist
            st.write("User Playlist Songs:")
            for song in user_songs:
                st.write(f"Song: {song['name']} by {song['artist']}")

            # Fetch recommendation playlist
            recommended_songs = []
            playlist_id = '5FErlA0FTU3PrLQo5MFj47'  # Your recommendation playlist ID
            playlist_tracks = sp.playlist_tracks(playlist_id)

            for track in playlist_tracks['items']:
                song_name = track['track']['name']
                artist_name = track['track']['artists'][0]['name']
                artist_id = track['track']['artists'][0]['id']
                track_id = track['track']['id']
                genres = sp.artist(artist_id)['genres']
                
                # Get audio features for each track in recommendation playlist
                audio_features = get_audio_features(track_id)

                recommended_songs.append({
                    'name': song_name,
                    'artist': artist_name,
                    'features': audio_features,
                    'genres': genres
                })

            # Normalize features and calculate Euclidean distance for recommendations
            st.write("Recommended Songs:")
            all_genres = list(all_genres)  # Convert genre set to list for consistency

            # Prepare feature vectors with audio features + genre vectors
            user_song_vectors = [
                song['features'] + genre_vector(song['genres'], all_genres) for song in user_songs
            ]
            recommended_song_vectors = [
                song['features'] + genre_vector(song['genres'], all_genres) for song in recommended_songs
            ]

            # Normalize feature vectors for Euclidean distance calculation
            scaler = StandardScaler()
            user_song_vectors = scaler.fit_transform(user_song_vectors)
            recommended_song_vectors = scaler.transform(recommended_song_vectors)

            # Calculate Euclidean distances and get top recommendations
            distances = cdist(user_song_vectors, recommended_song_vectors, metric='euclidean')
            top_recommendations = np.argsort(distances.flatten())[:10]  # Get 10 closest matches

            # Display top recommended songs
            for index in top_recommendations:
                song_index = index % len(recommended_songs)  # Adjust index based on flattening
                song = recommended_songs[song_index]
                st.write(f"Song: {song['name']} by {song['artist']} (Genres: {', '.join(song['genres'])})")
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
