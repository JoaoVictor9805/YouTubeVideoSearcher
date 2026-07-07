import requests
import os
from dotenv import load_dotenv

load_dotenv()

def buscarVideos(pesquisa: str):
    
    API_Key = os.getenv("YOUTUBE_API_KEY")
    url = "https://www.googleapis.com/youtube/v3/search"

    parametros = {
        "part": "snippet",
        "q": pesquisa,
        "key": API_Key,
        "maxResults": 15,
        "type": "video"
    }

    respostaAPI = requests.get(url, params=parametros)
    respostaJSON = respostaAPI.json()

    listaLimpa = []

    for item in respostaJSON["items"]:
        titulo  = item["snippet"]["title"]
        canal   =  item["snippet"]["channelTitle"]
        thumb   = item["snippet"]["thumbnails"]["default"]["url"]
        video_id      = item["id"]["videoId"]

        video = {
            "titulo": titulo,
            "canal": canal,
            "thumb": thumb,
            "video_id": video_id
        }

        listaLimpa.append(video)

    return listaLimpa
