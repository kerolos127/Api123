from fastapi import APIRouter, Depends
from executor import execute_command
from auth import verify_api_key
from logger import log

router = APIRouter()

@router.post("/exec")
def exec_command(cmd: str, api_key: str = Depends(verify_api_key)):
    log(f"command executed: {cmd}")
    return execute_command(cmd)