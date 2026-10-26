from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

import os # Used for keeping environment variable secret

import database  # Import the database module
import plaid_functions  # Import the plaid module


### Setup Vars###
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

database.setup_database()
ph = PasswordHasher()

### Models ###
class User(BaseModel):
    username: str
    password: str



### ROUTES ###

###GET ROUTES###
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(request, 'index.html', {'title': 'Home'})


@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"title": "Login", "signin": "login"})

@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"title": "Register", "signin": "register"})

    
@app.get("/dashboard")#TODO add authentication to this route so that only logged in users can access it
def dashboard(request: Request):
    public_token = plaid_functions.plaid_sandbox_request_public_token()
    access_token = plaid_functions.plaid_exchange_public_token(public_token)
    accounts = plaid_functions.plaid_get_accounts(access_token)
    return templates.TemplateResponse(request, "dashboard.html", {"title": "Dashboard", "accounts": accounts})


#### POST ROUTES ###

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # login logic goes here later
    user = database.get_user(username)
    if user and ph.verify(user["password"], password):
        return RedirectResponse("/dashboard", status_code=303)
    else:
        return templates.TemplateResponse(request, "login.html", {"title": "Login", "error": "Invalid username or password"})

@app.post("/register")
def register(request: Request, username: str = Form(...), password: str = Form(...)):
    # Check if the username already exists
    existing_user = database.get_user(username)
    if existing_user:
        return templates.TemplateResponse(request, "login.html", {"title": "Register", "error": "Username already exists", "signin": "/register"})

    # Hash the password and create the user
    hashed_password = ph.hash(password)
    database.create_user(username, hashed_password)

    return RedirectResponse("/dashboard", status_code=303)
