from sqlalchemy import Column, String, Integer, Float,ForeignKey, Boolean
from BaseModel import BaseModel, Status,Base
from sqlalchemy.orm import relationship
class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float)
    currency = Column(String)
   
class Product(BaseModel):
    __tablename__ = 'products'
    name = Column(String, nullable=False)
    description = Column(String)
    price_id = Column(Integer, ForeignKey('prices.id'))
    price = relationship('Price')
    stock = Column(Integer)
    category = Column(String)
    sku = Column(String)
    weight = Column(Float)
    dimensions = Column(String)
    manufacturer = Column(String)
    is_available = Column(Boolean, default=True)

    def is_in_stock(self) -> bool:
        return self.stock > 0

    def apply_discount(self, percentage: float) -> None:
        self.price.amount -= self.price.amount * (percentage / 100)
