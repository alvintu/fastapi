from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

db  = []

class City(BaseModel):
    name: str
    timezone: str

@app.get('/')
def index():
    return {'key' : 'value'}


@app.get('/cities')
def get_cities():
    # results = []
    # for city in db:
    url =  "https://api.windy.com/api/webcams/v2/list/nearby=46.54,7.98,5?show=webcams:location,image"
    headers = {"x-windy-key": "vzxwperNgGGmvtjKxsaVZ2ctgi3cr1N3"}
    r = requests.get(url, headers=headers)

    print(r.json())
    return db


@app.get('/cities/{city_id}')
def get_city(city_id: int):
    return db[city_id-1]


@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]



@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id - 1)
    return {}

