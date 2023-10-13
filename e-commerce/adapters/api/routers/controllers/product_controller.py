from typing import List

from controllers.database import get_db
# Importaciones de entidades y casos de uso
from entities.product import Product as ProductModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from use_cases.product_use_cases import (
    add_product as uc_add_product, delete_product as uc_delete_product,
    edit_product as uc_edit_product,
    get_product_details as uc_get_product_details,
    list_products as uc_list_products,
    search_products_by_name_or_category as uc_search_products,
    )

router = APIRouter()


@router.post("/products/", response_model=ProductModel, status_code=201)
def add_product(product: ProductModel, db: Session = Depends(get_db)):
    """Agregar un nuevo producto."""
    return uc_add_product(product, db)


@router.put("/products/{product_id}", response_model=ProductModel)
def edit_product(
    product_id: int, product: ProductModel, db: Session = Depends(get_db)
    ):
    """Editar un producto existente."""
    return uc_edit_product(product_id, product, db)


@router.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Eliminar un producto."""
    uc_delete_product(product_id, db)
    return {"detail": "Product deleted successfully"}


@router.get("/products/", response_model=List[ProductModel])
def list_products(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
    ):
    """Listar todos los productos."""
    return uc_list_products(skip, limit, db)


@router.get(
        "/products/search/{name_or_category}", response_model=List[ProductModel]
        )
def search_products_by_name_or_category(
    name_or_category: str, db: Session = Depends(get_db)
    ):
    """Buscar productos por nombre o categoría."""
    return uc_search_products(name_or_category, db)


@router.get("/products/{product_id}", response_model=ProductModel)
def get_product_details(product_id: int, db: Session = Depends(get_db)):
    """Obtener detalles de un producto específico."""
    return uc_get_product_details(product_id, db)
