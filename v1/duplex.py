from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class Message(BaseModel):
    message: str

from .manager import ws_manager
duplex_router = APIRouter()
templates = Jinja2Templates(directory='templates')

@duplex_router.get('/')
def route(request: Request, response_classe= HTMLResponse):
    try:
        return templates.TemplateResponse(
            'duplex.html', {"request":request}
        )
    except:
        import traceback
        formatted_lines = traceback.format_exc().splitlines()
        message = '\n'.join(formatted_lines)
        print(f"LOG[ERROR] {message}")

@duplex_router.websocket('/ws/duplex/{user}')
async def push_endpoint(websocket: WebSocket, user: str):
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await ws_manager.broadcast(data)
    except (WebSocketDisconnect, Exception):
        ws_manager.disconnect(websocket)