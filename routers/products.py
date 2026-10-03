from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas import ProductCreate, ProductResponse, ProductUpdate
import crud


router = APIRouter()


# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# CREATE
@router.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)


# READ
@router.get(
    "/products",
    response_model=list[ProductResponse]
)
def read_products(
    db: Session = Depends(get_db)
):
    return crud.read_products(db)


# UPDATE
@router.put(
    "/products/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    updated_product = crud.update_product(
        db,
        product_id,
        product
    )

    if updated_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated_product


# DELETE
@router.delete(
    "/products/{product_id}",
    response_model=ProductResponse
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    deleted_product = crud.delete_product(
        db,
        product_id
    )

    if deleted_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return deleted_product