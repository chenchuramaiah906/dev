from fastapi import FastAPI

app = FastAPI()

@app.get("/order")
def read_order():
    return {"order_id": 101, "item": "Wireless Mouse", "price": 499}
