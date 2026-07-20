from fastapi import WebSocket, APIRouter

router = APIRouter(prefix="/ws", tags=["realtime"])

@router.websocket("/class/{class_id}")
async def class_websocket(websocket: WebSocket, class_id: int):
    await websocket.accept()
    await websocket.send_text(f"Connected to class {class_id}. Screen share and interruptions ready.")
    # TODO: Handle screen share signaling, interruptions, chat
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except:
        pass
