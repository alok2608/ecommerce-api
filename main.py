from fastapi import FastAPI
from routers import products, orders

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "E-commerce API is live and running "}

app.include_router(products.router)
app.include_router(orders.router)
