from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items: Dict[int, Item] = {
    1: Item(name="Notebook", description="A simple spiral notebook", price=3.99),
    2: Item(name="Pencil", description="Graphite pencil for writing", price=0.99),
}

@app.get("/items")
def list_items():
    """Return all available items."""
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Return a single item by its ID."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items", status_code=201)
def create_item(item: Item):
    """Create a new item and return it."""
    new_id = max(items.keys(), default=0) + 1
    items[new_id] = item
    return {"id": new_id, **item.dict()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an existing item by its ID."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.dict()}
