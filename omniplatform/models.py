from sqlalchemy import ForeignKey, Column, String, Integer, Numeric
from sqlalchemy.orm import relationship, backref

from database import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, unique=True)


class Variant(Base):
    __tablename__ = "variants"

    variant_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    title = Column(String(255))
    UPC = Column(String(12), nullable=False, unique=True)
    SKU = Column(String(8), nullable=False, unique=True)
    list_price = Column(Numeric)

    product = relationship("Product", backref=backref("products"))
