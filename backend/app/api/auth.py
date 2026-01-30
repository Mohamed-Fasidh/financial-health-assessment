
from fastapi import APIRouter
from app.schemas.auth import Login
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login")
def login(data: Login):
    token = create_access_token({"sub": data.email})
    return {"access_token": token, "token_type": "bearer"}
