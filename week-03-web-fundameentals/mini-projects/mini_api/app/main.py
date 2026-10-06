from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

products = [
    {"product_id" : 101, "name" : "Dust pan", "category" : "cleaning" , "in_stock" : True},
    {"product_id": 102, "name" : "pen", "category" : "stationary" , "in_stock" : False},
    {"product_id": 103, "name" : "flower vase", "category" : "decoration", "in_stock" : True}
]

class addProduct(BaseModel):
    name : str
    category : str
    in_stock : bool

class ProductAdded(BaseModel):
    id : int
    name : str
    category : str
    in_stock : bool


@app.get("/products")
def gel_all_products():
    return products

@app.get("/products/{product_id}")
def get_a_product(product_id : int):
    for prod in products:
        if prod["product_id"] == product_id:
            return prod
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


@app.post("/products", status_code=status.HTTP_201_CREATED)
def add_product(product : addProduct):
    new_name = product.name.strip().lower()
    for prod in products:
        if prod["name"].strip().lower() == new_name:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = f"Product with the name {product.name} already exists"
            )
    id = products[-1]["product_id"] + 1 if products else 101
    name = product.name
    category = product.category
    in_stock = product.in_stock
    new_product = {"product_id" : id, "name" : name, "category" : category, "in_stock" : in_stock}
    products.append(new_product)
    return {"message" : f"product {name} with id {id} is created successfully"}



@app.put("/products/{product_id}")
def update_a_product(product_id : int, payload: addProduct):
    for prod in products:
        if prod["product_id"] == product_id:
            prod["name"] = payload.name
            prod["category"] = payload.category
            prod["in_stock"] = payload.in_stock
            return prod
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail='Product not found'
    )



@app.delete("/products/{product_id}")
def delete_a_product(product_id : int):
    for prod in products:
        if prod["product_id"] == product_id:
            products.remove(prod)
            return products
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail="Product not dound"
    )