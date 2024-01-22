import os
import sys
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    accepted = Column(Boolean)
    follower_id = Column(Integer, ForeignKey('users.id'))
    follower = relationship('User', foreign_keys=[follower_id])
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', foreign_keys=[user_id])

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    photo = Column(String(50))
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    comments = relationship('Comment')

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e