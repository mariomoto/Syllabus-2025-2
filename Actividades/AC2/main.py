import collections
from os.path import join
from utilidades import Anime  # IMPORTANT: Debes utilizar esta nametupled
from collections import defaultdict


#####################################
#       Parte I - Cargar datos      #
#####################################
def cargar_animes(ruta_archivo: str) -> list:
    # TODO: Completar
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        animes = []
        for line in file:
            nombre, capitulos, puntaje, estreno, estudio, generos = line.strip().split(",")
            animes.append(Anime(
                nombre=str(nombre),
                capitulos=int(capitulos),
                puntaje=int(puntaje),
                estreno=int(estreno),
                estudio=str(estudio),
                generos=set(generos.split(";")),
            ))
    return animes


#####################################
#        Parte II - Consultas       #
#####################################
def animes_por_estreno(animes: list) -> dict:
    # TODO: Completar
    animes_por_estreno = dict()
    for anime in animes:
        if anime.estreno not in animes_por_estreno:
            animes_por_estreno[anime.estreno] = []
        animes_por_estreno[anime.estreno].append(anime.nombre)
    return animes_por_estreno


def descartar_animes(generos_descartados: set, animes: list) -> list:
    # TODO: Completar
    return [anime.nombre for anime in animes if not anime.generos & generos_descartados
    ]


def resumen_animes_por_ver(*animes: Anime) -> dict:
    # TODO: Completar
    resumen = {}
    resumen = {"puntaje promedio": 0.0, "capitulos total": 0, "generos": set()}
    for anime in animes:
        resumen["puntaje promedio"] += int(anime.puntaje)
        resumen["capitulos total"] += int(anime.capitulos)
        resumen["generos"] = resumen["generos"].union(anime.generos)
    if len(animes) > 0:
        resumen["puntaje promedio"] = resumen["puntaje promedio"] / len(animes)
    return resumen


def estudios_con_genero(genero: str, **estudios: dict) -> list:
    # TODO: Completar
    resultado = []
    for estudio, animes in estudios.items():
        for anime in animes:
            if genero in anime.generos:
                resultado.append(estudio)

    return resultado


if __name__ == "__main__":
    #####################################
    #       Parte I - Cargar datos      #
    #####################################
    animes = cargar_animes(join("data", "ejemplo.chan"))
    indice = 0
    for anime in animes:
        print(f"{indice} - {anime}")
        indice += 1

    #####################################
    #        Parte II - Consultas       #
    #####################################
    # Solo se usará los 2 animes del enunciado.
    datos = [
        Anime(
            nombre="Hunter x Hunter",
            capitulos=62,
            puntaje=9,
            estreno=1999,
            estudio="Nippon Animation",
            generos={"Aventura", "Comedia", "Shonen", "Acción"},
        ),
        Anime(
            nombre="Sakura Card Captor",
            capitulos=70,
            puntaje=10,
            estreno=1998,
            estudio="Madhouse",
            generos={"Shoujo", "Comedia", "Romance", "Acción"},
        ),
    ]

    # animes_por_estreno
    estrenos = animes_por_estreno(datos)
    print(estrenos)
    
    # descartar_animes
    animes = descartar_animes({"Comedia", "Horror"}, datos)
    print(animes)
    
    # resumen_animes_por_ver
    resumen = resumen_animes_por_ver(datos[0], datos[1])
    print(resumen)

    # estudios_con_genero
    estudios = estudios_con_genero(
        "Shonen",
        Nippon_Animation=[datos[0]],
        Madhouse=[datos[1]],
    )
    print(estudios)
