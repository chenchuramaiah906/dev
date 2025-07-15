from fastapi import FastAPI

app = FastAPI()

@app.get("/payment")
def read_payment():
    return {"payment_id": 202, "status": "paid", "method": "UPI"}
