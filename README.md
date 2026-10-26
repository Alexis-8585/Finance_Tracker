# Finance Tracker

A web app that lets a user log in once and view accounts from multiple banks in one place. Built with Python and FastAPI, with bank data pulled through the Plaid API.

> **Status: work in progress.** The app currently runs against Plaid's sandbox with dummy data. It is not production-ready, and it should not be used with real bank credentials.

## What works today

- User login form with server-rendered pages (FastAPI + Jinja2)
- Passwords hashed with Argon2 (no plain-text storage)
- PostgreSQL database for users and account data
- Plaid sandbox integration that displays test account data on the site

## Planned

- Session-based authentication and protected routes (the dashboard is currently reachable without logging in)
- User signup flow
- Transaction history and spending summaries
- Connecting multiple institutions per user
- Better styling 
- Tests

## Tech stack

| Area | Tools |
| --- | --- |
| Backend | Python, FastAPI, Uvicorn |
| Templates | Jinja2, HTML, CSS |
| Database | PostgreSQL, psycopg |
| Auth | Argon2 (`argon2-cffi`) |
| Bank data | Plaid API (sandbox) |


## Project structure

```
app.py          # FastAPI routes
database.py     # Database connection and queries
plaid_functions.py #Handles connections to the Plaid API
templates/      # Jinja2 HTML templates
static/css/     # Stylesheets
```

## Security notes

- Passwords are hashed with Argon2 before being stored.
- Secrets are loaded from environment variables, not hard-coded.

## What I learned

- Server-side rendering with FastAPI and Jinja2, and how the Post/Redirect/Get pattern works for form submissions
- Password hashing and why plain-text comparison is unsafe
- Managing secrets with environment variables and virtual environments
- Working with a third-party financial API (Plaid)
