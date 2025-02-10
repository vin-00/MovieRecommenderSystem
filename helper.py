from dotenv import load_dotenv
import requests
import os

load_dotenv()

api_key = os.getenv("API_KEY")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id,api_key)
    response = requests.get(url)
    data = response.json()

    return "http://image.tmdb.org/t/p/w500"+data['poster_path']
