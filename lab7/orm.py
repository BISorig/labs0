from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine('sqlite:///products.db')

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

category1 = Category(name='Electronics')
product1 = Product(name='Laptop', price=1000.0, category=category1)
product2 = Product(name='Smartphone', price=500.0, category=category1)

category2 = Category(name='Clothing')
product3 = Product(name='T-Shirt', price=20.0, category=category2)

session.add(category1)
session.add(category2)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print(f"Category: {category.name}")
    for product in category.products:
        print(f" - Product: {product.name}, Price: {product.price}")

product3.category = category1
session.commit()

session.delete(category2)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print(f"Category: {category.name}")
    for product in category.products:
        print(f" - Product: {product.name}, Price: {product.price}")
