from fastapi import APIRouter, WebSocket
from typing import Dict

router = APIRouter(prefix="/webrtc", tags=["screen-share"])

active_rooms: Dict = {}

@router.websocket("/room/{room_id}")
async def webrtc_signaling(websocket: WebSocket, room_id: str):
    await websocket.accept()
    if room_id not in active_rooms:
        active_rooms[room_id] = []
    active_rooms[room_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_json()
            # Broadcast to others in room (screen share ICE candidates, offers, etc.)
            for client in active_rooms[room_id]:
                if client != websocket:
                    await client.send_json(data)
    except:
        active_rooms[room_id].remove(websocket)
