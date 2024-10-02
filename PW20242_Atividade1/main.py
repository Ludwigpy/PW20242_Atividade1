from re import template
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

app = FastAPI()

# ... (restante do seu código)

@app.get("/cadastro") # type: ignore
async def cadastro(request: Request):
    return template.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro") # type: ignore
async def post_cadastro(request: Request, nome: str = Form(...), descricao: str = Form(...),
                         estoque: int = Form(...), preco: float = Form(...), categoria: str = Form(...)):
    
    print(nome, descricao, estoque, preco, categoria)  
    return RedirectResponse("/")