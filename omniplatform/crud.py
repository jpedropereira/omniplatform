from sqlalchemy.orm import Session
import models
import schemas


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product_by_name(db: Session, product_title: str):
    return db.query(models.Product).filter(models.Product.title==product_title).first()


def create_product(db: Session, product: schemas.ProductCreate):
    new_product = models.Product(title=product.title)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_variants(db: Session):
    return db.query(models.Variant).all()


def create_variant(db: Session, variant: schemas.VariantCreate, product_id: int):
    new_variant = models.Variant(**variant.dict(), product_id=product_id)
    db.add(new_variant)
    db.commit()
    db.refresh(new_variant)
    return new_variant
