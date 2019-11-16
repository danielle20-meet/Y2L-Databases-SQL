from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Product(Base):
	"""table"""
	__tablename__ ="Products"
	name= Column(String)
	price= Column(Float)
	picture=Column(String)
	desc=Column(String)
	id =Column(Integer,primary_key=True)
class Cart(Base):
	__tablename__="Cart"
	id=Column(Integer,primary_key=True)
	Productid=Column(Integer)

		
