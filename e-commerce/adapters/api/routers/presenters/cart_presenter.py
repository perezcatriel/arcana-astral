from typing import List, Union

from entities.cart import Cart as CartModel


class CartPresenter:

    @staticmethod
    def present_cart_item(cart_item: CartModel) -> dict:
        return {
            "id": cart_item.id,
            "user_id": cart_item.user_id,
            "product_id": cart_item.product_id,
            "quantity": cart_item.quantity,
            "created_at": cart_item.created_at.isoformat(),
            "updated_at": cart_item.updated_at.isoformat() if cart_item.updated_at else None
            }

    @staticmethod
    def present_cart_items(cart_items: List[CartModel]) -> List[dict]:
        return [CartPresenter.present_cart_item(cart_item) for cart_item in
                cart_items]

    @staticmethod
    def present_response(data: Union[CartModel, List[CartModel]]) -> dict:
        if isinstance(data, list):
            cart_items = CartPresenter.present_cart_items(data)
            return {
                "data": cart_items,
                "meta": {
                    "count": len(cart_items)
                    }
                }
        else:
            cart_item = CartPresenter.present_cart_item(data)
            return {
                "data": cart_item
                }
