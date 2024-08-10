from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from UserModel import User, Address
from ProductModel import Product, Price
from BaseModel import Base, Status

def main():
    #engine = create_engine('sqlite:///:memory:')
    engine = create_engine('sqlite:///my_database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    #---------------Adding sample address----------------
    address1 = Address(street="Eczacıbaşı", city='Kartal',zip_code="12345")
    address2 = Address(street="Atatürk", city='Maltepe',zip_code="12346")
    address3 = Address(street="Kordon", city='Pendik',zip_code="12347")
    #--------------------------------------------------
    
    #---------------Adding sample users----------------
    user1 = User(address=address1,username='johndoe', email='john@example.com', password='securepassword', first_name='John', last_name='Doe', age=30, phone_number='1234567890')
    user2 = User(address=address2,username='janedoe', email='jane@example.com', password='securepassword', first_name='Jane', last_name='Doe', age=25, phone_number='0987654321')
    user3 = User(address=address3,username='alice', email='alice@example.com', password='securepassword', first_name='Alice', last_name='Smith', age=28, phone_number='1122334455')

    session.add_all([address1,address2,address3,user1, user2, user3])
    session.commit()
    #----------------------------------------------------
    
    #---------------query users--------------------------
    queried_user1 = session.query(User).filter_by(username='johndoe').first()
    queried_user2 = session.query(User).filter_by(username='janedoe').first()
    queried_user3 = session.query(User).filter_by(username='alice').first()
    
    print(queried_user1.created_at)
    print(queried_user2.updated_at)
    print(queried_user3.status)
    
    print(queried_user1.address.street)
    print(queried_user2.address.city)
    print(queried_user3.address.zip_code)
    #----------------------------------------------------
    
    #--------------- Adding sample products--------------
    price1 = Price(amount=99.99, currency='USD')
    price2 = Price(amount=199.99, currency='USD')
    price3 = Price(amount=299.99, currency='USD')
    
    product1 = Product(name='Laptop', description='A powerful laptop', price=price1, stock=10, category='Electronics', sku='LAP123', weight=2.5, dimensions='30x20x2 cm', manufacturer='TechCorp')
    product2 = Product(name='Smartphone', description='A high-end smartphone', price=price2, stock=20, category='Electronics', sku='SMP456', weight=0.5, dimensions='15x7x0.7 cm', manufacturer='PhoneInc')
    product3 = Product(name='Tablet', description='A versatile tablet', price=price3, stock=15, category='Electronics', sku='TAB789', weight=1.0, dimensions='25x17x0.8 cm', manufacturer='TabCorp')

    session.add_all([price1, price2, price3, product1, product2, product3])
    session.commit()
    #------------------------------------------------------
    
    #---------------query products-------------------------
    queried_product1 = session.query(Product).filter_by(name='Laptop').first()
    queried_product2 = session.query(Product).filter_by(name='Smartphone').first()
    queried_product3 = session.query(Product).filter_by(name='Tablet').first()
    print(queried_product1.status)
    print(queried_product2.updated_at)
    print(queried_product3.updated_at)
    print(queried_product1.price.amount)
    print(queried_product1.price.currency)
    print(queried_product2.is_available)
    print(queried_product3.price_id)
    
    print(queried_product3.status)
    print(queried_product3.created_at)
    print(queried_product3.updated_at)
    print(queried_product3.price_id)
    print(queried_product3.price.amount)
    #--------------------------------------------------------- 
if __name__ == '__main__':
    main()
