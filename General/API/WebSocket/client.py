from websockets.sync.client import connect

def hello():
    uri = "ws://localhost:8765"
    with connect(uri) as websocket:
        websocket.send("Alice")
        print(">>> Alice")
        greeting = websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    hello()
