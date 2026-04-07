from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import RedirectResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1,
        "titulo": "Meu primeiro post",
        "resumo": "Resumo...",
        "conteudo": "Conteúdo completo...",
        "autor": "Carlos"
    }
]