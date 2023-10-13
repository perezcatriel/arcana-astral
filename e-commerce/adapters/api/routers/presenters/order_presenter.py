from typing import List, Union

from entities.order import Order as OrderModel


class OrderPresenter:

    @staticmethod
    def present_order(order: OrderModel) -> dict:
        return {
            "id": order.id,
            "user_id": order.user_id,
            "status": order.status,
            "total_amount": order.total_amount,
            "created_at": order.created_at.isoformat(),
            "updated_at": order.updated_at.isoformat() if order.updated_at else None
            }

    @staticmethod
    def present_orders(orders: List[OrderModel]) -> List[dict]:
        return [OrderPresenter.present_order(order) for order in orders]

    @staticmethod
    def present_response(data: Union[OrderModel, List[OrderModel]]) -> dict:
        if isinstance(data, list):
            orders = OrderPresenter.present_orders(data)
            return {
                "data": orders,
                "meta": {
                    "count": len(orders)
                    }
                }
        else:
            order = OrderPresenter.present_order(data)
            return {
                "data": order
                }
