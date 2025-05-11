# Harmony Blend: Personalized Song Recommendation System

## Project Description
**Harmony Blend** is a personalized song recommendation system built using the Spotify API. The system analyzes the audio features of songs in a given playlist and recommends new songs with similar attributes. The project uses a combination of **Euclidean distance** and **audio features** such as danceability, energy, tempo, and genre to generate recommendations. This helps users discover music that aligns with the vibe and style of their current playlist.

## Features
- **Song Recommendations**: Generate song suggestions based on a given playlist.
- **Euclidean Distance**: Utilizes Euclidean distance to measure the similarity between songs.
- **Audio Features**: Incorporates various Spotify audio features including danceability, energy, key, loudness, and more.
- **Genre and Artist Filtering**: Considers genre and artist information to refine recommendations.

Data- The song data is gathered from the Spotify API.
The dataset includes information such as song name, artist, genres, and audio features like danceability, energy, tempo, and more.
Model Used- Euclidean Distance: The recommendation model calculates the similarity between songs based on their audio features using the Euclidean distance formula.
