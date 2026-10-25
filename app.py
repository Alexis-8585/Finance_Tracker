from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


import os # Used for keeping environment variable secret



### Setup Vars###
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

### Models ###
class User(BaseModel):
    username: str
    password: str

first = User(username="test", password="test123")


### Routes ###
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(request, 'index.html', {'title': 'Home'})


@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html")


@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # login logic goes here later
    if username == first.username and password == first.password:
        return RedirectResponse("/dashboard", status_code=303)
    else:
        return templates.TemplateResponse(request, "login.html", {"error": "Invalid username or password"})

    
@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(request, "dashboard.html")