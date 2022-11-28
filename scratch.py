import websockets
import asyncio

async def listen():
    url = ""



    async with websocket.connect(url) as websocket:
            msg = await websocket.rcv()
            print(msg)

asyncio.get_event_loop().run_until_complete
(listen())

