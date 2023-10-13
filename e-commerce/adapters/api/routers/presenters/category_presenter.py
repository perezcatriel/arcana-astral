from typing import List, Union

from entities.category import Category as CategoryModel


class CategoryPresenter:

    @staticmethod
    def present_category(category: CategoryModel) -> dict:
        return {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "created_at": category.created_at.isoformat(),
            "updated_at": category.updated_at.isoformat() if category.updated_at else None
            }

    @staticmethod
    def present_categories(categories: List[CategoryModel]) -> List[dict]:
        return [CategoryPresenter.present_category(category) for category in
                categories]

    @staticmethod
    def present_response(
        data: Union[CategoryModel, List[CategoryModel]]
        ) -> dict:
        if isinstance(data, list):
            categories = CategoryPresenter.present_categories(data)
            return {
                "data": categories,
                "meta": {
                    "count": len(categories)
                    }
                }
        else:
            category = CategoryPresenter.present_category(data)
            return {
                "data": category
                }
