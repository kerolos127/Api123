from fastapi import APIRouter, WebSocket
import subprocess

router = APIRouter()

@router.websocket("/terminal")
async def terminal(ws: WebSocket):
    await ws.accept()
    while True:
        cmd = await ws.receive_text()
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate()
        await ws.send_text(stdout + stderr)