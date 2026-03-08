from fastapi import APIRouter, Depends
from auth import verify_api_key
import os

router = APIRouter()

@router.get("/list")
def list_files(path: str = ".", api_key: str = Depends(verify_api_key)):
    return os.listdir(path)

@router.get("/read")
def read_file(path: str, api_key: str = Depends(verify_api_key)):
    with open(path, "r") as f:
        return {"content": f.read()}

@router.post("/write")
def write_file(path: str, content: str, api_key: str = Depends(verify_api_key)):
    with open(path, "w") as f:
        f.write(content)
    return {"status": "written"}