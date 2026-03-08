from fastapi import APIRouter
from api_keys import generate_api_key
import psutil
import platform

router = APIRouter()

@router.post("/create_key")
def create_key(owner: str):
    return {"api_key": generate_api_key(owner)}

@router.get("/info")
def system_info():
    return {
        "system": platform.system(),
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent
    }