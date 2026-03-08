from fastapi import FastAPI
import terminal, files, system, tools, websocket_terminal, example_plugin

app = FastAPI(
    title="Exos Terminal API V5",
    version="5.0",
    description="Ultimate Terminal API with Plugins and WebSocket"
)

app.include_router(terminal.router, prefix="/terminal")
app.include_router(files.router, prefix="/files")
app.include_router(system.router, prefix="/system")
app.include_router(tools.router, prefix="/tools")
app.include_router(websocket_terminal.router)

@app.get("/")
def root():
    return {"name": "Exos Terminal API V5", "version": "5.0", "author": "@HackerExos"}