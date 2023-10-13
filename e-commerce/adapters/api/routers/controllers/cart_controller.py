from typing import List

from controllers.database import get_db
# Importaciones de entidades y casos de uso
from entities.cart import Cart as CartModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from use_cases.cart_use_cases import (
    add_product_to_cart as uc_add_product_to_cart, empty_cart as uc_empty_cart,
    remove_product_from_cart as uc_remove_product_from_cart,
    update_cart_item_quantity as uc_update_cart_item_quantity,
    view_cart_content as uc_view_cart_content,
    )

router = APIRouter()


@router.post("/cart/", response_model=CartModel, status_code=201)
def add_product_to_cart(cart_item: CartModel, db: Session = Depends(get_db)):
    """Agregar un producto al carrito."""
    return uc_add_product_to_cart(cart_item, db)


@router.delete("/cart/{cart_item_id}", status_code=204)
def remove_product_from_cart(cart_item_id: int, db: Session = Depends(get_db)):
    """Eliminar un producto del carrito."""
    uc_remove_product_from_cart(cart_item_id, db)
    return {"detail": "Product removed from cart successfully"}


@router.put("/cart/{cart_item_id}", response_model=CartModel)
def update_cart_item_quantity(
    cart_item_id: int, quantity: int, db: Session = Depends(get_db)
    ):
    """Actualizar la cantidad de un producto en el carrito."""
    return uc_update_cart_item_quantity(cart_item_id, quantity, db)


@router.get("/cart/{user_id}", response_model=List[CartModel])
def view_cart_content(user_id: int, db: Session = Depends(get_db)):
    """Ver el contenido del carrito de un usuario."""
    return uc_view_cart_content(user_id, db)


@router.delete("/cart/empty/{user_id}", status_code=204)
def empty_cart(user_id: int, db: Session = Depends(get_db)):
    """Vaciar el carrito de un usuario."""
    uc_empty_cart(user_id, db)
    return {"detail": "Cart emptied successfully"}
