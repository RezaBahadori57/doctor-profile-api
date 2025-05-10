from fastapi import FastAPI
from auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Doctor Appointment API",
    version="1.0.0",
    description="API for user authentication and appointment scheduling system"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])


@app.get("/")
def read_root():
    return {"message": "Doctor Appointment API is running 🚀"}

