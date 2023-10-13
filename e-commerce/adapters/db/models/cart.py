from sqlalchemy import Column, ForeignKey, Integer, CheckConstraint
from sqlalchemy.orm import relationship

from application_adapters.repositories.db.database import Base


class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, index=True, nullable=False)

    # Asegurarse de que la cantidad siempre sea positiva
    CheckConstraint('quantity > 0', name='quantity_positive')

    user = relationship("User", back_populates="carts")
    product = relationship("Product", back_populates="carts")

    def __repr__(self):
        return f"<Cart(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity})>"
