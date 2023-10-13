from typing import List, Union

from entities.user import User as UserModel


class UserPresenter:

    @staticmethod
    def present_user(user: UserModel) -> dict:
        """
        Presenta un único usuario.
        """
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            # No incluimos la contraseña ni otros datos sensibles
            "is_admin": user.is_admin,
            "created_at": user.created_at.isoformat(),
            "updated_at": user.updated_at.isoformat() if user.updated_at else None
            }

    @staticmethod
    def present_users(users: List[UserModel]) -> List[dict]:
        """
        Presenta una lista de usuarios.
        """
        return [UserPresenter.present_user(user) for user in users]

    @staticmethod
    def present_response(data: Union[UserModel, List[UserModel]]) -> dict:
        """
        Presenta una respuesta estándar que puede contener un usuario o una lista de usuarios.
        """
        if isinstance(data, list):
            users = UserPresenter.present_users(data)
            return {
                "data": users,
                "meta": {
                    "count": len(users)
                    }
                }
        else:
            user = UserPresenter.present_user(data)
            return {
                "data": user
                }
