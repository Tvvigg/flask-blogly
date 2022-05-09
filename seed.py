"""Seed file to make sample data"""

from codecs import utf_16_be_decode
from models import db, User, Post, PostTag, Tag
from app import app

#Create all tables
db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()
PostTag.query.delete()
Tag.query.delete()

u1 = User(first_name="Becky", last_name="Sue")
u2 = User(first_name="Tom", last_name="Foo")
u3 = User(first_name="Steve", last_name="Lue")

db.session.add_all([u1, u2, u3])
db.session.commit()

t1 = Tag(name="TGIF")
t2 = Tag(name="TBT")

db.session.add_all([t1, t2])
db.session.commit()


