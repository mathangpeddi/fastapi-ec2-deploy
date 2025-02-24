# main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()
db_file = "orders.db"

# Initialize the SQLite database and orders table
def init_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            order_type TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Pydantic model for incoming order data
class Order(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

# POST endpoint to create a new order
@app.post("/orders")
def create_order(order: Order):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (symbol, price, quantity, order_type) VALUES (?, ?, ?, ?)",
        (order.symbol, order.price, order.quantity, order.order_type)
    )
    conn.commit()
    conn.close()
    return {"message": "Order created successfully"}

# GET endpoint to retrieve all orders
@app.get("/orders", response_model=List[Order])
def get_orders():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, price, quantity, order_type FROM orders")
    rows = cursor.fetchall()
    conn.close()
    return [Order(symbol=row[0], price=row[1], quantity=row[2], order_type=row[3]) for row in rows]

# Bonus: WebSocket for real-time order status updates
clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # For now, simply echo the received message
            await websocket.send_text(f"Received: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)

