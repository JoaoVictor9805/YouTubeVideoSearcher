# Dependências

## FastAPI

Framework web responsável por organizar a aplicação.

Responsabilidades:
- Criar rotas (URLs)
- Receber requisições HTTP
- Validar dados
- Executar a lógica da aplicação
- Retornar respostas ao cliente


o FastAPI é responsável por organizar as rotas e decidir qual função executar;
O FastAPI é responsável pelo protocolo HTTP (receber a requisição, localizar a rota correta e montar a resposta HTTP). Minha função é responsável apenas por produzir o conteúdo da resposta.

---

## Uvicorn

Servidor ASGI responsável por executar a aplicação FastAPI.

Responsabilidades:
- Escutar uma porta (ex.: localhost:8000)
- Receber requisições do navegador
- Encaminhá-las para o FastAPI
- Enviar a resposta de volta ao navegador


o Uvicorn é responsável por criar e manter o servidor HTTP;

---

## Seu código

Responsabilidades:
- implementar a lógica da aplicação;
- decidir o que retornar.

o código é responsável pela lógica da aplicação (como retornar "Olá, mundo!").

---

# Comandos utilizados no Bash:

- python -m venv .venv
- source /c/Users/joaov/Desktop/Faculdade/projetosFerias/youtubeDownloader/.venv/Scripts/activate ou source .venv/Scripts/activate
- pip install fastapi uvicorn
- pip freeze > requirements.txt
- uvicorn app.main:application --reload // está criando o servidor http para que possa ser acessado via navegador


# Respostas importantes aos comandos:

- Uvicorn running on http://127.0.0.1:8000