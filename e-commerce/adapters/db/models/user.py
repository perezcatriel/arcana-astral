from application_adapters.repositories.db.database import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    orders = relationship("Order", back_populates="user")
    carts = relationship("Cart", back_populates="user", uselist=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, hashed_password={self.hashed_password}, is_active={self.is_active}, is_admin={self.is_admin})>"
