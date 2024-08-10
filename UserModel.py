from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from BaseModel import BaseModel, Status,Base

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String)
    city = Column(String)
    zip_code = Column(String)
    #user = relationship('User', back_populates='address')
class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String,  nullable=False)#unique=True, error for same data 
    email = Column(String,  nullable=False)#unique=True,error for same data
    address_id=Column(Integer, ForeignKey('addresses.id'))
    address = relationship('Address')
    #address = relationship('Address', back_populates='user', viewonly=True)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    phone_number = Column(String)
    is_verified = Column(Boolean, default=False)
    

    def is_adult(self) -> bool:
        return self.age >= 18

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
