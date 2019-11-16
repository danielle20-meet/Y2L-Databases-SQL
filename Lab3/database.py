from model import Base, Product , Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def addpro(name,price,pic,desc):
	pro_obj=Product(
		name=name,
		price=price,
		picture=pic,
		desc=desc)
	session.add(pro_obj)
	session.commit()
def edit(id,newd):
	pro=session.query(Product).filter_by(id=id).first()
	pro.name=newd
	session.commit()

def query_all():
   """
   Print all the students
   in the database.
   """
   pro = session.query(
      Product).all()
   return pro
def re_id(id):
   """
   return a product 
   """
   pro = session.query(
      Product).filter_by(id=id).first()
   return pro
def del_id(id):
	session.query(Product).filter_by(id=id).delete()
	session.commit()
def add_cort(Productid):
	cart=Cart(Productid=Productid)
	session.add(cart)
	session.commit()
