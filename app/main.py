from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request

application = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@application.get("/")
def home(request: Request, pesquisa: str = ""):

    listaVideos = [
        {
            "titulo": "Curso de FastAPI",
            "canal": "João",
            "duracao": "15 min"
        },
        {
            "titulo": "Aprendendo Python",
            "canal": "Hashtag Programação",
            "duracao": "40 min"
        },
        {
            "titulo": "DDD na prática",
            "canal": "Full Cycle",
            "duracao": "1h20"
        }
    ]
    
    return templates.TemplateResponse(request=request, name="index.html", context={"pesquisa": pesquisa, "listaVideos": listaVideos})