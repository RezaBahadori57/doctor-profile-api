from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi_sso.sso.facebook import FacebookSSO
from starlette.config import Config
from config import get_db
from models import User
import os

router = APIRouter()
config = Config(".env")
FACEBOOK_CLIENT_ID = config("FACEBOOK_CLIENT_ID", cast=str)
FACEBOOK_CLIENT_SECRET = config("FACEBOOK_CLIENT_SECRET", cast=str)

sso = FacebookSSO(
    client_id=FACEBOOK_CLIENT_ID,
    client_secret=FACEBOOK_CLIENT_SECRET,
    redirect_uri="http://localhost:8000/auth/facebook/callback"
)

@router.get("/auth/facebook/login")
async def facebook_login():
    return await sso.get_login_redirect()

@router.get("/auth/facebook/callback")
async def facebook_callback(request: Request, db=Depends(get_db)):
    user_info = await sso.verify_and_process(request)


    user = db.users.find_one({"facebook_id": user_info.user_id})
    if not user:
        db.users.insert_one({
            "facebook_id": user_info.user_id,
            "email": user_info.email,
            "name": user_info.display_name
        })


    return {"message": "Facebook login successful", "user": user_info.dict()}


def facebook_sso():
    return None


def oauth2_scheme():
    return None