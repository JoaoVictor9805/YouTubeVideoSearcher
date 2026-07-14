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
        titulo      = item["snippet"]["title"]
        canal       = item["snippet"]["channelTitle"]
        thumb       = item["snippet"]["thumbnails"]["high"]["url"]
        video_id    = item["id"]["videoId"]

        video = {
            "titulo": titulo,
            "canal": canal,
            "thumb": thumb,
            "video_id": video_id
        }

        listaLimpa.append(video)

    return listaLimpa


def buscarVideo(video_id: str):

    API_Key = os.getenv("YOUTUBE_API_KEY")
    url = "https://www.googleapis.com/youtube/v3/videos"

    parametros = {
        "part": "snippet",
        "id": video_id,
        "key": API_Key
    }

    respostaAPI = requests.get(url, params=parametros)
    respostaJSON = respostaAPI.json()

    if not respostaJSON["items"]:
        return None
    
    else:
        item = respostaJSON["items"][0]

        thumb = item["snippet"]["thumbnails"]

        if "maxres" in thumb:
            thumb = thumb["maxres"]["url"]
        else:
            thumb = thumb["default"]["url"]


        video = {
            "titulo":   item["snippet"]["title"],
            "canal":    item["snippet"]["channelTitle"],
            "thumb":    thumb,
            "video_id": item["id"]
        }

        return video
