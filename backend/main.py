from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import models
from db.database import engine
from routers import user, search
from db.router_impl import db_user
from auth import authentication

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(search.router)

@app.on_event("startup")
async def create_admin():
    db_user.create_admin()


models.Base.metadata.create_all(engine)