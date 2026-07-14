import yt_dlp

def criarOpcoes():
    return {
        "cookiefile": "cookies.txt"
    }


def buscarFormatos(video_id: str):

    url = f"https://www.youtube.com/watch?v={video_id}"
    
    ytdlp = yt_dlp.YoutubeDL(criarOpcoes())

    info = ytdlp.extract_info(url, download=False)
    
    
    ## for formato in info["formats"]:
    ##    print(
    ##        formato["format_id"],   ## id
    ##        formato["ext"],         ## mp4... 
    ##        formato.get("height"),  ## 1080p... (qualidade imagem)
    ##        formato.get("vcodec"),  ## formato de compressão do vídeo (nulo se for apenas áudio)
    ##        formato.get("acodec")   ## formato de compressão do áudio
    ## )
        
    listaFormatos = {"videos": {}, "audios": {}}
    
    for formato in info["formats"]:
    
        if formato["vcodec"] != "none":

            if formato["ext"] not in listaFormatos["videos"]: 
                listaFormatos["videos"][formato["ext"]] = [{"format_id": formato["format_id"], "height": formato.get("height")}]

            else:
                listaFormatos["videos"][formato["ext"]] += [{"format_id": formato["format_id"], "height": formato.get("height")}]

        
        if formato["acodec"] != "none" and formato["vcodec"] == "none":

            if formato["ext"] not in listaFormatos["audios"]:
                listaFormatos["audios"][formato["ext"]] = [{"format_id": formato["format_id"], "abr": formato.get("abr")}]

            else:
                listaFormatos["audios"][formato["ext"]] += [{"format_id": formato["format_id"], "abr": formato.get("abr")}]


    for extensao in listaFormatos["videos"]:
        listaFormatos["videos"][extensao] = sorted(listaFormatos["videos"][extensao], key=lambda formato: formato["height"], reverse=True)

    for extensao in listaFormatos["audios"]:
        listaFormatos["audios"][extensao] = sorted(listaFormatos["audios"][extensao], key=lambda formato: formato["abr"], reverse=True)


    for extensao in listaFormatos["videos"]:
        resolucoesVistas = set()
        listaFinal = []

        for formato in listaFormatos["videos"][extensao]:
            if formato["height"] not in resolucoesVistas:
                listaFinal.append(formato)
                resolucoesVistas.add(formato["height"])
            
        listaFormatos["videos"][extensao] = listaFinal

    for extensao in listaFormatos["audios"]:
        resolucoesVistas = set() 
        listaFinal = []

        for formato in listaFormatos["audios"][extensao]:
            if formato["abr"] not in resolucoesVistas:
                listaFinal.append(formato)
                resolucoesVistas.add(formato["abr"])
        
        listaFormatos["audios"][extensao] = listaFinal

    return listaFormatos


def downloadVideo(video_id: str, format_id: str, extensao: str):

    url = f"https://www.youtube.com/watch?v={video_id}"

    opcoes = criarOpcoes()
    opcoes["format"] = f"{format_id}+bestaudio"
    opcoes["outtmpl"] = "downloads/%(title)s.%(ext)s" ##output template 
    opcoes["merge_output_format"] = extensao
    
    ytdlp = yt_dlp.YoutubeDL(opcoes)

    ytdlp.extract_info(url, download=True)


def downloadAudio(video_id: str, format_id: str, extensao: str):

    print("=== DOWNLOAD AUDIO ===")
    print("Extensão:", extensao)
    print("Format ID:", format_id)

    url = f"https://www.youtube.com/watch?v={video_id}"

    opcoes = criarOpcoes()
    opcoes["format"] = format_id
    opcoes["outtmpl"] = "downloads/%(title)sAudio.%(ext)s"

    if extensao == "mp3":
        opcoes["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ]

    ytdlp = yt_dlp.YoutubeDL(opcoes)

    ytdlp.extract_info(url, download=True)
