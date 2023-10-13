from typing import List

from controllers.database import get_db
# Importaciones de entidades y casos de uso
from entities.order import Order as OrderModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from use_cases.order_use_cases import (
    cancel_order as uc_cancel_order, create_order as uc_create_order,
    get_order_details as uc_get_order_details,
    list_user_orders as uc_list_user_orders,
    update_order_status as uc_update_order_status,
    )

router = APIRouter()


@router.post("/order/", response_model=OrderModel, status_code=201)
def create_order(order: OrderModel, db: Session = Depends(get_db)):
    """Crear una nueva orden."""
    return uc_create_order(order, db)


@router.get("/order/{order_id}", response_model=OrderModel)
def get_order_details(order_id: int, db: Session = Depends(get_db)):
    """Ver detalles de una orden."""
    return uc_get_order_details(order_id, db)


@router.get("/orders/user/{user_id}", response_model=List[OrderModel])
def list_user_orders(user_id: int, db: Session = Depends(get_db)):
    """Listar todas las órdenes de un usuario."""
    return uc_list_user_orders(user_id, db)


@router.put("/order/cancel/{order_id}", status_code=204)
def cancel_order(order_id: int, db: Session = Depends(get_db)):
    """Cancelar una orden."""
    uc_cancel_order(order_id, db)
    return {"detail": "Order canceled successfully"}


@router.put("/order/status/{order_id}", response_model=OrderModel)
def update_order_status(
    order_id: int, status: str, db: Session = Depends(get_db)
    ):
    """Actualizar el estado de una orden."""
    return uc_update_order_status(order_id, status, db)
