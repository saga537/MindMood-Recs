import requests

# TMDB API Key
TMDB_API_KEY = "45b038515f78f17aecb3db8656954204"

def get_movie_recommendations(theme):
    keyword_url = f"https://api.themoviedb.org/3/search/keyword?api_key={TMDB_API_KEY}&query={theme}"
    response = requests.get(keyword_url, timeout=10)
    data = response.json()

    if not data['results']:
        return []

    keyword_id = data['results'][0]['id']

    discover_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_keywords={keyword_id}&sort_by=popularity.desc"
    movies = requests.get(discover_url).json()

    return movies.get('results', [])[:5]


def get_book_recommendations(theme):
    url = f"https://www.googleapis.com/books/v1/volumes?q={theme}&maxResults=5"
    response = requests.get(url)
    data = response.json()
    return data.get('items', [])


