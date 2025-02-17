# vue3-fastapi-oath2-jwt-demo
This is a Demo project to show how to do OAuth2 token auth with FastAPI to Vue3 frontend with JWT forked from sdairs/vue3-fastapi-oath2-jwt-demo

The project consists of:
- A backend API built using Python & FastAPI
- A frontend UI built using Vue.js
- A database using MySQL with SQLAlchemy 1.4 interface

sadir's demo is a good starting point for understanding how the components interact.

## Backend API
The backend is a REST API built in Python and using FastAPI.

Uses: 
- Pydantic (validation between frontend input & backend output, conversion from DB ORM models)
- SQLAlchemy
- python-jose is used for working with JWT
- passlib is used for handling password hashing

The API exposes two endpoints:
- `GET /` returns a JSON Hello World result, protected by OAuth2
- `POST /token` takes multi-part form data providing credentials for logging in & returns an OAuth2 bearer token

You can run the backend using the uvicorn auto-reloading dev server, make sure you're inside the `backend` dir e.g.

`~/vue3-fastapi-oath2-jwt-demo/backend $ uvicorn main:app --reload --port 8080` 

This command would serve your backend on `http://localhost:8080`.
You can add `--host 0.0.0.0` if you want to serve it on your network.

## Frontend UI
The frontend is a Vue3.js app that presents a very basic Login form with Username & Password fields.

Uses:
- Vue3.js for app framework 
- Element-Plus as UI framework
- VueX for state management
- Vue-router for handling routing
- Native Fetch API for communication with the backend REST API
- Yarn for dependency management
- Parcel is used for bundling

There is only a single route `/` which presents a simple Login form.
Clicking the Submit button will `POST` to the `/token` backend endpoint, giving the Username & Password as multi-part form data.

Included in the package.json is two `parcel` commands.
```
    "start": "parcel serve ./src/index.html",
    "build": "parcel build --no-scope-hoist ./src/index.html"
```

You can execute these with `yarn run start` and `yarn run build` (you must be within the `frontend` directory.

The `yarn run start` command will launch an auto-reloading dev webserver to serve the frontend on `http://localhost:1234`.

## Database
The database used is this fork is a simple MySQL file.

Running `python database/database.py` from the `backend` directory will initiate the database with a users table with the follow user;

Username: `user1`
Password: `P@ss12345`

Passwords are stored as hashes.
