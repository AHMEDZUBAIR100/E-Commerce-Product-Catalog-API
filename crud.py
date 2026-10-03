from sqlalchemy.orm import Session

from models import Product
from schemas import ProductCreate, ProductUpdate


# CREATE
def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

# READ
def read_products(db: Session):
    return db.query(Product).all()

