from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os

from app.services.youtube import buscarVideos
from fastapi.staticfiles import StaticFiles

application = FastAPI()
templates = Jinja2Templates(directory="app/templates")

static_dir = os.path.join(os.path.dirname(__file__), "static")
application.mount("/static", StaticFiles(directory=static_dir), name="static")

@application.get("/")
def home(request: Request, pesquisa: str = ""):

    listaVideos = buscarVideos(pesquisa)

    return templates.TemplateResponse(request=request, name="index.html", context={"pesquisa": pesquisa, "listaVideos": listaVideos})

@application.get("/download/{video_id}")
def download(request: Request, video_id: str):
    
    return templates.TemplateResponse(request=request, name="download.html", context={})