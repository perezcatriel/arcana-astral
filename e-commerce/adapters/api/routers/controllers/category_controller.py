from typing import List

from controllers.database import get_db
# Importaciones de entidades y casos de uso
from entities.category import Category as CategoryModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from use_cases.category_use_cases import (
    add_category as uc_add_category, delete_category as uc_delete_category,
    edit_category as uc_edit_category,
    get_products_by_category as uc_get_products_by_category,
    list_categories as uc_list_categories,
    )

router = APIRouter()


@router.post("/category/", response_model=CategoryModel, status_code=201)
def add_category(category: CategoryModel, db: Session = Depends(get_db)):
    """Agregar una nueva categoría."""
    return uc_add_category(category, db)


@router.put("/category/{category_id}", response_model=CategoryModel)
def edit_category(
    category_id: int, category: CategoryModel, db: Session = Depends(get_db)
    ):
    """Editar una categoría existente."""
    return uc_edit_category(category_id, category, db)


@router.delete("/category/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """Eliminar una categoría."""
    uc_delete_category(category_id, db)
    return {"detail": "Category deleted successfully"}


@router.get("/categories/", response_model=List[CategoryModel])
def list_categories(db: Session = Depends(get_db)):
    """Listar todas las categorías."""
    return uc_list_categories(db)


@router.get(
        "/category/products/{category_id}", response_model=List[CategoryModel]
        )
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    """Obtener productos de una categoría específica."""
    return uc_get_products_by_category(category_id, db)
