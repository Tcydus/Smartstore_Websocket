import websockets
import asyncio
import json 

class WebSocketClient():

    def __init__(self):
        pass

    async def connect(self):
        '''
        
            Connecting to webSocket server

            websockets.client.connect returns a WebSocketClientProtocol, which is used to send and receive messages

        '''
        SERVER_IP = "192.168.1.50"
        SERVER_PORT = "5555"
        SERVER_URL = "ws://" + SERVER_IP + ":" + SERVER_PORT

        self.connection = await websockets.client.connect(SERVER_URL)
        if self.connection.open:
            print('Connection stablished. Client correcly connected')
            # Send greeting
            message = self.json_massage("Hey server, this is webSocket client")
            await self.sendMessage(message)
            return self.connection

    def json_massage(self,message):
        return json.dumps({"client" : message,"request" : 1})
    
    async def sendMessage(self, message):
        '''
            Sending message to webSocket server
        '''
        await self.connection.send(message)

    async def receiveMessage(self, connection):
        '''
            Receiving all server messages and handling them
        '''
        while True:
            try:
                message = await connection.recv()
                # data = json.load(message)
                print('Received message from server: ' + str(message))
                
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break

    async def heartbeat(self, connection):
        '''
        Sending heartbeat to server every 5 seconds
        Ping - pong messages to verify connection is alive
        '''
        while True:
            try:
                ping = self.json_massage("ping")
                await connection.send(ping)
                await asyncio.sleep(5)
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break
          

if __name__ == '__main__':
    # Creating client object
    client = WebSocketClient()
    loop = asyncio.get_event_loop()
    # Start connection and get client connection protocol
    connection = loop.run_until_complete(client.connect())
    # Start listener and heartbeat 
    tasks = [
        asyncio.ensure_future(client.heartbeat(connection)),
        asyncio.ensure_future(client.receiveMessage(connection)),
    ]

    loop.run_until_complete(asyncio.wait(tasks))