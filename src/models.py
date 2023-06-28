import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("follower.follow_to_id"))
    username = Column(String(250), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False )
    post = relationship('Post', backref="user")
    comment = relationship('Comment', backref="user")
    messages = relationship('Messages', backref="user")

class Follower(Base):
    __tablename__ = 'follower'
    follow_from_id = Column(Integer, nullable=True)
    follow_to_id = Column(Integer, primary_key=True)

class Create(Base):
    __tablename__ = 'create'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    create_id = Column(Integer, ForeignKey("comment.id"))
    post_id = Column(Integer, ForeignKey("post.id"))



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    create_id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    author_id = Column(Integer, nullable=False)

class Messages(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    messages_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String(250), nullable=False)



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
