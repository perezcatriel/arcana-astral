from typing import List, Union

from entities.product import Product as ProductModel


class ProductPresenter:

    @staticmethod
    def present_product(product: ProductModel) -> dict:
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "category_id": product.category_id,
            "created_at": product.created_at.isoformat(),
            "updated_at": product.updated_at.isoformat() if product.updated_at else None
            }

    @staticmethod
    def present_products(products: List[ProductModel]) -> List[dict]:
        return [ProductPresenter.present_product(product) for product in
                products]

    @staticmethod
    def present_response(data: Union[ProductModel, List[ProductModel]]) -> dict:
        if isinstance(data, list):
            products = ProductPresenter.present_products(data)
            return {
                "data": products,
                "meta": {
                    "count": len(products)
                    }
                }
        else:
            product = ProductPresenter.present_product(data)
            return {
                "data": product
                }
