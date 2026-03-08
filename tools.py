from fastapi import APIRouter, Depends
from auth import verify_api_key
from tool_registry import list_tools, run_tool
from executor import execute_command

router = APIRouter()

@router.get("/list")
def tools_list(api_key: str = Depends(verify_api_key)):
    return list_tools()

@router.post("/run")
def run_tool_api(name: str, api_key: str = Depends(verify_api_key)):
    cmd = run_tool(name)
    if not cmd:
        return {"error": "tool not found"}
    return execute_command(cmd)