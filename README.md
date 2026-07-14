# 🎥 YouTube Downloader

Uma aplicação web desenvolvida com **FastAPI** que integra a **YouTube Data API v3** e a biblioteca **yt-dlp**, permitindo pesquisar vídeos do YouTube e realizar downloads em diferentes formatos e qualidades por meio de uma interface simples e intuitiva.

O projeto foi desenvolvido com foco em praticar conceitos de desenvolvimento web, integração com APIs, renderização de templates, manipulação dinâmica do DOM com JavaScript e processamento de mídia utilizando ferramentas externas.

---

## 📸 Demonstração

> *Adicione aqui um GIF ou algumas capturas de tela da aplicação.*

---

## ✨ Funcionalidades

- 🔎 Pesquisa de vídeos utilizando a **YouTube Data API v3**
- 📃 Exibição dos resultados da pesquisa
- 🖼️ Visualização de miniatura, título e canal dos vídeos
- 🎞️ Download de vídeos em diferentes:
  - formatos (MP4, WebM, etc.)
  - resoluções disponíveis
- 🎵 Download de áudio em:
  - MP3 (conversão via FFmpeg)
  - M4A
  - WebM
- 📋 Detecção automática dos formatos disponíveis para cada vídeo
- 🔄 Preservação da navegação do usuário ao retornar para a página de pesquisa

---

## 🔄 Como funciona

O projeto utiliza duas ferramentas principais para oferecer a experiência completa de pesquisa e download:

### YouTube Data API v3

Responsável por realizar a pesquisa dos vídeos a partir do termo informado pelo usuário, retornando informações como:

- título;
- canal;
- miniatura;
- ID do vídeo.

Esses dados são utilizados para montar a interface de resultados da aplicação.

### yt-dlp

Após o usuário selecionar um vídeo, a biblioteca **yt-dlp** é utilizada para:

- consultar todos os formatos disponíveis para download;
- identificar resoluções e bitrates disponíveis;
- realizar o download do conteúdo selecionado;
- converter arquivos de áudio para MP3 utilizando o FFmpeg quando necessário.

Essa divisão de responsabilidades torna a aplicação mais organizada e aproveita o melhor de cada ferramenta.

---

## 🛠️ Tecnologias utilizadas

- Python
- FastAPI
- Jinja2
- HTML5
- CSS3
- JavaScript
- YouTube Data API v3
- yt-dlp
- FFmpeg

---

## 📂 Estrutura do projeto

```text
youtubeDownloader/
│
├── app/
│   ├── services/
│   ├── static/
│   ├── templates/
│   └── main.py
│
├── downloads/
├── requirements.txt
└── README.md
```

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/youtube-downloader.git

cd youtube-downloader
```

---

### 2. Crie um ambiente virtual

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Instale o FFmpeg

O FFmpeg é utilizado para converter arquivos de áudio para MP3.

Após a instalação, certifique-se de que ele esteja disponível no **PATH** do sistema.

---

### 5. Configure a API do YouTube

Este projeto utiliza a **YouTube Data API v3** para realizar pesquisas de vídeos.

1. Acesse o **Google Cloud Console**.
2. Crie um projeto.
3. Ative a **YouTube Data API v3**.
4. Gere uma chave de API.
5. Crie um arquivo chamado `.env` na raiz do projeto:

```env
YOUTUBE_API_KEY=SUA_CHAVE_AQUI
```

### 6. Execute a aplicação

```bash
uvicorn app.main:application --reload
```

Depois acesse:

```
http://127.0.0.1:8000
```

---

## 📌 Dependências

O projeto faz uso das seguintes ferramentas:

- **FastAPI** para o backend da aplicação;
- **Jinja2** para renderização dos templates HTML;
- **YouTube Data API v3** para pesquisa dos vídeos;
- **yt-dlp** para consulta dos formatos disponíveis e download dos conteúdos;
- **FFmpeg** para conversão de áudio para MP3.

---

## ⚠️ Observações

- A disponibilidade dos formatos depende do vídeo selecionado e das restrições impostas pelo YouTube.
- Alguns vídeos podem exigir cookies válidos para permitir o download de determinados formatos.
- Para downloads em MP3 é necessário possuir o FFmpeg instalado.
- O projeto utiliza uma chave da YouTube Data API v3, que **não acompanha o repositório**. Cada usuário deverá gerar sua própria chave para utilizar a aplicação.

---

## 🎯 Objetivos do projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos importantes de Engenharia de Software, entre eles:

- desenvolvimento de aplicações web utilizando FastAPI;
- integração com APIs REST;
- utilização da YouTube Data API v3;
- manipulação de formulários e eventos utilizando JavaScript;
- renderização de templates com Jinja2;
- organização da aplicação em camadas de serviço;
- processamento e conversão de mídia utilizando yt-dlp e FFmpeg.

---

## 📚 Principais aprendizados

Durante o desenvolvimento deste projeto foi possível aprofundar conhecimentos em diferentes áreas do desenvolvimento de software, incluindo:

- Desenvolvimento de aplicações web utilizando **FastAPI**;
- Consumo de APIs REST por meio da **YouTube Data API v3**;
- Integração de bibliotecas externas para processamento de mídia com **yt-dlp**;
- Conversão de arquivos de áudio utilizando **FFmpeg**;
- Renderização de páginas dinâmicas com **Jinja2**;
- Manipulação do DOM e atualização dinâmica da interface utilizando **JavaScript**;
- Organização da aplicação em camadas para separar responsabilidades entre rotas, serviços e templates;
- Gerenciamento de variáveis de ambiente para armazenamento seguro de credenciais;
- Tratamento de diferentes formatos e qualidades de mídia disponibilizados pelo YouTube;
- Integração entre frontend e backend para construção de uma experiência de usuário mais fluida.

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado.