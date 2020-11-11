import asyncio
import websockets
import json 

async def client_func():
    uri = "ws://localhost:1302"
    async with websockets.connect(uri) as websocket:
        barcode ="8850006901656"

        await websocket.send(json.dumps({"barcode" : barcode,"request" : 0}))
        
        print(f"sending   >>> {barcode}")

        
    


loop = asyncio.get_event_loop()
loop.run_until_complete(client_func())


loop.close()


print("End process")