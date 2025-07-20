from fastapi import APIRouter, Query
from bson import ObjectId
from database import db
from schemas.product import ProductCreate
from utils.pagination import get_pagination

router = APIRouter()


@router.post("/products", status_code=201)
async def create_product(product: ProductCreate):
    result = await db.products.insert_one(product.dict())
    return {"id": str(result.inserted_id)}


@router.get("/products")
async def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)
):
    query = {}

    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = db.products.find(query).skip(offset).limit(limit)
    products = []
    async for doc in cursor:
        products.append({
            "id": str(doc["_id"]),
            "name": doc["name"],
            "price": doc["price"]
        })

    return {
        "data": products,
        "page": get_pagination(offset, limit)
    }
