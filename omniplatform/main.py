from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get-products/", response_model=List[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return products


@app.post("/create-product/{title}", response_model=schemas.Product)
def create_product(title, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = crud.get_product_by_name(db=db, product_title=title)
    if new_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    return crud.create_product(db=db, product=product)
