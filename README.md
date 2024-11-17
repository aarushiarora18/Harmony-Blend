# Harmony Blend: Personalized Song Recommendation System

## Project Description
**Harmony Blend** is a personalized song recommendation system built using the Spotify API. The system analyzes the audio features of songs in a given playlist and recommends new songs with similar attributes. The project uses a combination of **Euclidean distance** and **audio features** such as danceability, energy, tempo, and genre to generate recommendations. This helps users discover music that aligns with the vibe and style of their current playlist.

## Features
- **Song Recommendations**: Generate song suggestions based on a given playlist.
- **Euclidean Distance**: Utilizes Euclidean distance to measure the similarity between songs.
- **Audio Features**: Incorporates various Spotify audio features including danceability, energy, key, loudness, and more.
- **Genre and Artist Filtering**: Considers genre and artist information to refine recommendations.

## Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.6 or later
- `pip` for installing dependencies

## Installation Instructions
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/harmony-blend.git
Install the required dependencies:
pip install -r requirements.txt
Create a Spotify Developer account (if you don't have one) and generate your Client ID and Client Secret from Spotify Developer Dashboard. Replace the placeholders in the main.py with your credentials.
Replace the placeholder your_playlist_id in the main.py file with the ID of the Spotify playlist you want to analyze.
python main.py
The program will output a CSV file (playlist_dataset.csv) containing the song data, including name, artist, genres, and relevant audio features.
The program will also recommend similar songs based on the playlist's features, generating a list of songs with similar characteristics.

Data- The song data is gathered from the Spotify API.
The dataset includes information such as song name, artist, genres, and audio features like danceability, energy, tempo, and more.
Model Used- Euclidean Distance: The recommendation model calculates the similarity between songs based on their audio features using the Euclidean distance formula.
