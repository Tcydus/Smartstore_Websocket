import sys, json
import asyncio
from websockets import connect

class WebsocketClass:
    async def __aenter__(self):
        # URI  = "ws://localhost:5555"
        SERVER_IP = "192.168.1.50"
        SERVER_PORT = "5555"
        SERVER_URL = "ws://" + SERVER_IP + ":" + SERVER_PORT
        self._conn  = connect(SERVER_URL)
        self.websocket = await self._conn.__aenter__()
        return self
    
    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)
    
    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        return await self.websocket.recv()

class StoreClient:
    def __init__(self):
       self.ws = WebsocketClass()
       self.loop = asyncio.get_event_loop()
    
    def get_barcode(self):
        return self.loop.run_until_complete(self.__async__get_barcode())
    
    async def __async__get_barcode(self):
        async with self.ws as echo:
            await echo.send(json.dumps({'ticks_history': 'R_50', 'end': 'latest', 'count': 1}))
            return await echo.receive()

    

if __name__ == "__main__":
    a = StoreClient()

    foo = a.get_barcode()
    print (foo)

    print ("async works like a charm!")

    foo = a.get_barcode()
    print (foo)
        
    
    