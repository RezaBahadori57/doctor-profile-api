from auth import oauth2_scheme
from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/appointments")
def get_appointments():
    return {"message": "Appointments endpoint"}



def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")
