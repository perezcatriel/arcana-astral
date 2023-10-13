from controllers.database import get_db
# Importaciones de entidades y casos de uso
from entities.user import User as UserModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from use_cases.user_use_cases import (
    change_password as uc_change_password, create_user as uc_create_user,
    delete_user as uc_delete_user, list_users as uc_list_users,
    login_for_access_token as uc_login, set_admin_status as uc_set_admin_status,
    update_user as uc_update_user,
    )

router = APIRouter()


@router.post("/register/", response_model=UserModel, status_code=201)
def create_user(user: UserModel, db: Session = Depends(get_db)):
    """Registro de un nuevo usuario."""
    return uc_create_user(user, db)


@router.post("/token/", tags=["Authentication"])
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
    ):
    """Inicio de sesión y obtención de token."""
    return uc_login(form_data, db)


@router.put("/users/{user_id}", response_model=UserModel)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    """Actualizar información de un usuario."""
    return uc_update_user(user_id, user, db)


@router.put("/users/{user_id}/change-password/")
def change_password(
    user_id: int, password_data: PasswordChange, db: Session = Depends(get_db)
    ):
    """Cambiar la contraseña de un usuario."""
    return uc_change_password(user_id, password_data, db)


@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Eliminar un usuario."""
    uc_delete_user(user_id, db)
    return {"detail": "User deleted successfully"}


@router.get("/users/", response_model=List[UserModel])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Listar usuarios."""
    return uc_list_users(skip, limit, db)


@router.put("/users/{user_id}/set-admin/", response_model=UserModel)
def set_admin_status(
    user_id: int, is_admin: bool, db: Session = Depends(get_db)
    ):
    """Asignar o revocar roles de administrador."""
    return uc_set_admin_status(user_id, is_admin, db)
