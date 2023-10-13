from application_adapters.repositories.db.database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    stock = Column(Integer, index=True)
    image = Column(String, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category', back_populates='products')
    carts = relationship('Cart', back_populates='product')

    def __repr__(self):
        return f'Product({self.id}, {self.name}, {self.description}, {self.price}, {self.stock}, {self.image}, {self.category_id})'
