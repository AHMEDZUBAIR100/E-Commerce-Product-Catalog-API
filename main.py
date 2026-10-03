from fastapi import FastAPI

from database import Base, engine
from routers.products import router as products_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="E-Commerce Product Catalog API"
)


app.include_router(products_router)