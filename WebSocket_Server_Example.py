# WebSocket server
import asyncio
import websockets

async def server(websocket, path):
    # Print out the IP and port of the newly connected client
    # print(f"New connection from {websocket.remote_address}")
    IP, Port, _, _ = websocket.remote_address
    print(f"Client with IP {IP} has connect on Port {Port}")

    # The server will keep handling this connection until the client disconnects
    while True:
        try:
            # Server waits for a message
            message = await websocket.recv()
            print(f"Received: {message}")
        
            # Server sends a response back to the client
            await websocket.send(message)

        except websockets.exceptions.ConnectionClosed:
            # print("Client {0} has disconnected".format(websocket.remote_address))
            IP, Port, _, _ = websocket.remote_address
            print(f"Client with IP {IP} had disconnected from Port {Port}")
            break

# Starts a new WebSocket server with the specified host and port
start_server = websockets.serve(server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)

# To stop the server via keyboard gracefully.
try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
finally:
    asyncio.get_event_loop().stop()
    print("Server stopped.")
