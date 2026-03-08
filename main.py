from fastapi import FastAPI
from api import terminal, files, system, tools, websocket_terminal

app = FastAPI(
    title="Exos Terminal API",
    version="4.0",
    description="Advanced Terminal Execution Platform"
)

app.include_router(terminal.router, prefix="/terminal")
app.include_router(files.router, prefix="/files")
app.include_router(system.router, prefix="/system")
app.include_router(tools.router, prefix="/tools")
app.include_router(websocket_terminal.router)

@app.get("/")
def root():
    return {
        "name": "Exos Terminal API",
        "version": "4.0",
        "author": "@HackerExos"
    }