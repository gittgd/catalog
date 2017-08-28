from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Gagan", email="gagan@udacity.com",
             picture='/static/logo.jpg')
session.add(user1)
session.commit()

# Items for Clothes
category1 = Category(name="Clothes", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Tops", user_id=1, description="Crafted from soft fabric for a relaxed fit, design features half sleeves pattern, round neck and cute print to the front. Pair with denim shorts and sandals for a cool, casual look.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Party Wear", user_id=1,  description="This items is sure to enhance her sophisticated charm. Perfect for parties and special occasions. Style it with delicate shoes and a trendy hair accessories to complete the look.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Nightwear", user_id=1, description="Comfortable night suit for your little one from the house. Allover teddy print on top along with soft waist pajamas makes the set look stylish. Round neck adds elegance of style to it. Made from soft fabric for maximum comfort all through the night.", category=category1)

session.add(item3)
session.commit()

# Items for Footwear
category2 = Category(name="Footwear", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="School Shoes", user_id=1, description="Designed for utmost comfort for those tiny feet of your little one. Ensures a formal look for the children. Buckle strap for perfect fit. Upper made of synthetic material and fabric lining. Durable PVC sole offer slip-resistance and durability.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Casual Shoes", user_id=1,  description="A range of super stylish & comfortable footwear, fine crafted from top quality material. Materials and components are carefully chosen for their quality and lightness, ensuring that no shoes are heavier than the proportional age appropriate weight for the child's body weight.", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Sandals", user_id=1, description="Perfect for a day out or a casual day, this pair is not only fashionable but also quite durable. Closed toe style makes it stylish. Velcro closure for comfort fit.", category=category2)

session.add(item3)
session.commit()

# Items for Toys
category3 = Category(name="Toys", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Musical Toys", user_id=1, description="Musical toys are totally safe for children and at the same time are fun loving and unique. They give children freedom to play while their imagination soar.They believe in spreading smiles on your children's faces always.", category=category3)

session.add(item1)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name