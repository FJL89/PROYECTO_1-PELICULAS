#http://127.0.0.1:8000

import pandas as pd
from fastapi import FastAPI
from typing import Optional
import numpy as np

app = FastAPI()

# cargar el dataset desde un archivo csv
df = pd.read_csv(r'DATOS/PLATAFORMAS RATINGS.csv')

from fastapi import FastAPI, Query

app = FastAPI()

#configuramos del inicios
@app.get("/")
async def index():
    return "ESTA ES LA APLICACION PARA CONSULTAS DE PELICULAS"

'''CONSULTA 1'''

# Definir endpoint para obtener la película con mayor duración
@app.get("/get_max_duration")
async def get_max_duration(year: int = Query(..., description="Año de estreno de la película"), 
                           platform: str = Query(..., description="Plataforma donde se encuentra la película"),
                           duration_type: str = Query(..., description="Tipo de duración de la película ('min')")):
    
    # Filtrar por año, plataforma y tipo de duración
    filtered = df[(df["release_year"] == year) & 
                  (df["platform"] == platform) & 
                  (df["duration_type"] == duration_type)]
    
    # Obtener la película con mayor duración
    max_duration_movie = filtered.loc[filtered["duration_int"].idxmax()]
    
    # Retornar los detalles de la película con mayor duración
    return f'LA PELICULA CON MAYOR DURACION DE LA PLATAFORMA {platform} PARA EL AÑO  {year} es: {max_duration_movie["title"]}'



'''CONSULTA N° 2'''

@app.get("/get_movie_count/")
async def get_movie_count(platform: str, score: float, year: int):
    filtered_df = df[(df['score'] > score) & (df['release_year'] == year) & (df['platform'] == platform)]
    if filtered_df.empty:
        return f"No hay películas en la plataforma {platform} con un puntaje mayor a {score} en el año {year}."
    else:
        grouped_df = filtered_df.groupby('platform')
        result = grouped_df.size().reset_index(name='count')
        count = result['count'].iloc[0]
        message = f"La cantidad de películas en {platform} con un puntaje mayor a {score} en el año {year} fue de {count}."
        return {"message": message}


'''CONSULTA N° 3'''
@app.get("/get_count_platform/")
def get_count_platform(platform: str):
    
    # Filtrar las películas por plataforma
    movies = df[df['id'].str.startswith(platform[0].lower())]
    
    # Contar la cantidad de películas por plataforma
    count = movies.shape[0]
    
    # Retornar el resultado
    return f' LA CANTIDAD DE PELICULAS PARA LA PLATAFORMA {platform} es de: {count}'

'''CONSULTA N° 4'''

@app.get("/get_actor/")
async def get_actor(platform: str, release_year: int):
    filtro = df[(df['platform'].str.contains(platform) & (df['release_year'] == release_year))]
    counts = filtro['cast'].str.split(',', expand=True).stack().str.strip().value_counts()
    actor_mas_comun = counts.idxmax()
    return f"El actor más común en la plataforma {platform} en el año {release_year} es {actor_mas_comun}"
