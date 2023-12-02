from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import logging

app = FastAPI()


movies: list = list()


class Film(BaseModel):
    id: int = None
    title: str = None
    description: str = None
    genre: str = None


movies.append(Film(id=0, title='Gone with the wind', description='About the civil war', genre='drama'))
movies.append(Film(id=1, title='Fight club', description='Guy tries to survive depression', genre='thriller'))
movies.append(Film(id=2, title='Saving private Rayan', description='Saving guy whose brothers died', genre='wardrama'))
movies.append(Film(id=3, title='Forest Gump', description='Mentally challenged guy gets lucky', genre='melodrama'))
movies.append(Film(id=4, title='Pulp Fiction', description='Criminals do what criminals do', genre='criminal'))
movies.append(Film(id=5, title='Hateful Eight', description='Bad people kill each other', genre='drama'))
movies.append(Film(id=6, title='Departed', description='Double agents are looking for each other', genre='policedrama'))
movies.append(Film(id=7, title='Nocturnal animals', description='Family robbed and killed', genre='drama'))
movies.append(Film(id=8, title='Stringer', description='Sociopath gets his way into news business', genre='thriller'))
movies.append(Film(id=10, title='Edge of tomorrow', description='Tom Cruise fights aliens', genre='action'))


@app.get('/film/genre/{genre}')
async def get_film_genre(genre: str):
    return list(filter(lambda x: (x.genre == genre), movies))
