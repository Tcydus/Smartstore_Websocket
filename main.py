#test api 
from store_client_new import WebSocketClient
import asyncio

async def main(my_client):
  while True :
    print("value : 0")
    print(my_client.get_barcode_list())
    await asyncio.sleep(2)

client = WebSocketClient()
loop = asyncio.get_event_loop()
connection = loop.run_until_complete(client.connect())
tasks = [
    asyncio.ensure_future(client.heartbeat(connection)),
    asyncio.ensure_future(client.receive_message(connection)),
    asyncio.ensure_future(main(client))

]

loop.run_until_complete(asyncio.wait(tasks))
