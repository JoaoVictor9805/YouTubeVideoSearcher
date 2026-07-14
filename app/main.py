from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os

from app.services.youtube import buscarVideos
from app.services.youtube import buscarVideo
from app.services.download import buscarFormatos
from app.services.download import downloadVideo
from app.services.download import downloadAudio

from fastapi.staticfiles import StaticFiles
from fastapi import Form
from fastapi.responses import RedirectResponse

application = FastAPI()
templates = Jinja2Templates(directory="app/templates")

static_dir = os.path.join(os.path.dirname(__file__), "static")
application.mount("/static", StaticFiles(directory=static_dir), name="static")

@application.get("/", name="index")
def home(request: Request, pesquisa: str = ""):

    listaVideos = buscarVideos(pesquisa)
    

    return templates.TemplateResponse(request=request, name="index.html", context={"pesquisa": pesquisa, "listaVideos": listaVideos})

@application.get("/download/{video_id}")
def mostrarPágina(request: Request, video_id: str):
    
    video = buscarVideo(video_id= video_id)
    
    if video is None:
        return templates.TemplateResponse(request=request, name="download.html", context={"video": None, "erro": "Vídeo não encontrado"})
    
    else:

        formatosDisponiveis = buscarFormatos(video_id= video_id)

        return templates.TemplateResponse(request=request, name="download.html", context={"video": video, "formatosDisponiveis": formatosDisponiveis})
    
@application.post("/download/{video_id}")
def baixarVideo(video_id: str,
                video_format: str | None = Form(None),
                video_quality: str | None = Form(None),
                audio_format: str | None = Form(None),
                audio_quality: str | None = Form(None)
                ):
    
    if video_format is not None and video_quality is not None:
        downloadVideo(video_id=video_id, format_id=video_quality, extensao=video_format)

    elif audio_format is not None and audio_quality is not None:
        downloadAudio(video_id=video_id, format_id=audio_quality, extensao=audio_format)

    return RedirectResponse(url=f"/download/{video_id}", status_code=303)