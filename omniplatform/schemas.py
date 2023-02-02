from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True


class VariantBase(BaseModel):
    title: str
    UPC: str
    SKU: str
    list_price: float


class VariantCreate(VariantBase):
    pass


class Variant(VariantBase):
    variant_id: int
    product_id: int

    class Config:
        orm_mode = True
