from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(product,price,quantity,description):
	product_object= Student(
		product=product,
		price=price,
		quantity=quantity,
		description=description)
	session.add(product_object)
	session.commit()

# create_product("skirt",30,3,"black")
# create_product("shorts",20,2,"white")

  

def update_product(product,price):
	product_object=session.query(
		Student).filter_by(
		product=product).first()
	product_object.price=price
	session.commit()
update_product("skirt",40)


def delete_product(id):
	session.query(Student).filter_by(
		id=2).delete()
	session.commit()
delete_product(2)


def get_product(id):
  pass


