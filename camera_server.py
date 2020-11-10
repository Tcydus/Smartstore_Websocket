import asyncio
import json
import logging
import websockets

logging.basicConfig()

class Server(object):

    def __init__(self, host, port):
        self.barcode = ""
        self.host, self.port = host, port
        self.loop = asyncio.get_event_loop()

        self.stop = self.loop.create_future()

        self.loop.run_until_complete(self.server())

    async def server(self):
        async with websockets.serve(self.ws_handler, self.host, self.port):
            await self.stop

    def json_massage(self,message):
        return json.dumps({"barcode" : message,"request" : 0})

    async def ws_handler(self, websocket, path):

        try:
            await websocket.send("555")
            await asyncio.sleep(2)
            # async for message in websocket:
            #     # data = json.loads(message)
            #     # if(data['request'] == 1 ):
            #     #     await websocket.send(self.json_massage(self.barcode) )
            #     #     self.barcode = ""
                    
            #     # else:
            #     #     self.barcode = data["barcode"]
            #     #     print(self.barcode)  
            #     print(message)
                
                
        except websockets.exceptions.ConnectionClosed:
            print('Client connection with server closed')
                     
        finally:
            print("Finally : ",websocket)


if __name__ == '__main__':    
    server = Server(host='localhost', port=5555)    
    # server = Server(host='192.168.1.50', port=5555)