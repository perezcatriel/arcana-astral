import datetime

from application_adapters.repositories.db.database import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_price = Column(Float)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f'<Order id={self.id} user_id={self.user_id} total_price={self.total_price} date={self.date}>'
