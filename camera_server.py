import asyncio
# import signal
import json
import logging
import websockets

logging.basicConfig()

class Server(object):

    def __init__(self, host, port):
        self.barcode = []
        self.host, self.port = host, port
        self.loop = asyncio.get_event_loop()

        self.stop = self.loop.create_future()
        # self.loop.add_signal_handler(signal.SIGINT, self.stop.set_result, None)

        self.loop.run_until_complete(self.server())

    async def server(self):
        async with websockets.serve(self.ws_handler, self.host, self.port):
            await self.stop

    async def ws_handler(self, websocket, path):
        # msg = await websocket.recv()
        # print(f'Received: {msg}', end = "\t")

        # msg = "Accept"
        # await websocket.send(msg)
        # print(f'Sending: {msg} ')

        try:
            async for message in websocket:
                # data = json.loads(message)
                # self.barcode = data["barcode"]
                # websocket.send()
        finally:
            print("Finally : ",websocket)
            # await unregister(websocket)

    
     



if __name__ == '__main__':
    # server = Server(host='localhost', port=5555)
    server = Server(host='192.168.1.50', port=5555)
