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

# UPDATE
def update_product(
    db: Session,
    product_id: int,
    product: ProductUpdate
):
    db_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if db_product is None:
        return None

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)

    return db_product
