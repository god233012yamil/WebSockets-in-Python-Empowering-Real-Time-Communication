"""
here's the revised Python WebSocket client code. The client will now 
receive input from stdin and continue until 'quit' is entered:

Here's what this code does:

It first establishes a connection to the server.
Then, it enters a while loop to keep the connection open.
It asks for input from the user.
If the user enters 'quit', it prints "Quitting..." and breaks the while 
loop, which closes the connection.
If the user enters something other than 'quit', it sends that message to 
the server and then waits for a response.
After receiving a response, it prints that response and then continues the 
while loop, asking for another input from the user.
Please make sure to run this script from a terminal or console because it 
requires input from stdin. Also note that if the server is not running or 
stops, the client will raise a ConnectionRefusedError.
"""

# WebSocket client
import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:  # keep connection open
            try:
                # get input from user
                message = input("Enter your message: ")

                # if user types 'quit', end the connection
                if message.lower() == 'quit':
                    print("Quitting...")
                    break

                # send message to the server
                await websocket.send(message)
                print(f"Transmit: {message}")

                # wait for a response
                message = await websocket.recv()
                print(f"Received: {message}")
            except websockets.exceptions.ConnectionClosed:
                print("server has disconnected")
                break  
            except websockets.exceptions.ConnectionClosed:
                print("server has disconnected")
                break  

# start the client and connect to the server
try:
    asyncio.get_event_loop().run_until_complete(client())
except KeyboardInterrupt:
    print("Program interrupted, stopping client...")
finally:
    print("Client stopped.")
