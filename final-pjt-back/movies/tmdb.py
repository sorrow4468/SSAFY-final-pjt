import requests
import json

class TMDBHelper:
    def __init__(self, api_key=None):
        self.api_key = api_key

    base_url = 'https://api.themoviedb.org/3'
    def get_request_url(self, method='/movie/popular', **kwargs):
        request_url = self.base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url
    

    def get_genre_url(self, method='/genre/movie/list'):
        genre_url = self.base_url + method
        genre_url += f"?api_key={self.api_key}&language=ko-KR"
        
        return  genre_url

tmdb_helper = TMDBHelper('__APIKEY__')

results = list()
movies_list = list()

# 장르정보 저장
genre_url = tmdb_helper.get_genre_url()
data = requests.get(genre_url).json()
genres = data.get('genres')
genre_list = []
for genre in genres:
    temp = {
        "model": "movies.genre",
        "pk": genre['id'],
        "fields": {
            "name": genre['name']
        }
    }
    genre_list.append(temp)
    
with open('genres.json', 'w', encoding="utf-8") as make_file:
    json.dump(genre_list, make_file, ensure_ascii=False, indent="\t")

# 영화정보 저장
for i in range(1, 21):
    request_url = tmdb_helper.get_request_url(
        region='KR', 
        language='ko',
        page = i
        )

    data = requests.get(request_url).json()
    results = data.get('results')

    for result in results:
        temp = {
            "model": "movies.movie",            
            "fields": {
                "title": result["title"],
                "release_date": result["release_date"],
                "popularity": result["popularity"],
                "vote_count": result["vote_count"],
                "vote_average": result["vote_average"],
                "overview": result["overview"],
                "poster_path": result["poster_path"],
                "genres": result["genre_ids"],

            }
        }
        movies_list.append(temp)

movies_list.sort(key=lambda x: x['fields']['release_date'])

# print(movies_list)

with open('movies.json', 'w', encoding="utf-8") as make_file:
    json.dump(movies_list, make_file, ensure_ascii=False, indent="\t")


# print(genres)

