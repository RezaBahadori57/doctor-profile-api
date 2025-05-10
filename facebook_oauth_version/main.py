from fastapi import FastAPI
from .auth import facebook_sso


app = FastAPI()
app.include_router(auth_router)
