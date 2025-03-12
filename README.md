# Movie Recommender System

## Overview
The **Movie Recommender System** is a content-based recommendation application built using **Streamlit**. It allows users to enter a movie name and specify the number of recommendations they want. The system then suggests movies based on similarities in genres, director, actors, and tags.

## Features
- Simple and user-friendly interface powered by **Streamlit**
- Content-based recommendation system
- Uses movie metadata such as **genres, director, actors, and tags**
- Generates recommendations based on similarity scores

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Enter the movie name and specify the number of recommendations.
3. View the recommended movies based on similarity.

## How It Works
- The system calculates movie similarity using **Text vectorization and cosine similarity**.
- It finds movies with similar genres, directors, actors, and tags.
- Based on the similarity scores, the top matching movies are recommended.

## Contributing
Feel free to fork the repository and submit pull requests to improve the recommender system.

## License
This project is licensed under the MIT License.

