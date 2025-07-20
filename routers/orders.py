from fastapi import APIRouter
from bson import ObjectId
from database import db
from schemas.order import OrderCreate
from utils.pagination import get_pagination

router = APIRouter()


@router.post("/orders", status_code=201)
async def create_order(order: OrderCreate):
    order_data = order.dict()
    result = await db.orders.insert_one(order_data)
    return {"id": str(result.inserted_id)}


@router.get("/orders/{user_id}")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = db.orders.find({"userId": user_id}).skip(offset).limit(limit)

    orders = []

    async for order in cursor:
        items = []
        total = 0.0
        for item in order["items"]:
            product = await db.products.find_one({"_id": ObjectId(item["productId"])})
            if product:
                price = product["price"]
                total += price * item["qty"]
                items.append({
                    "productDetails": {
                        "id": str(product["_id"]),
                        "name": product["name"]
                    },
                    "qty": item["qty"]
                })

        orders.append({
            "id": str(order["_id"]),
            "items": items,
            "total": round(total, 2)
        })

    return {
        "data": orders,
        "page": get_pagination(offset, limit)
    }
