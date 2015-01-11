import os
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, mapper

from domain.model import blog, generated

engine = create_engine(os.environ['DATABASE_URL'], echo=True)
Session = sessionmaker(bind=engine)

metadata = MetaData()

posts = Table(
        'post', metadata,
        Column('id', Integer, primary_key=True),
        Column('title', String),
        Column('body', String),
        Column('date', Date),
        Column('url', String, unique=True),
        Column('city', String))
mapper(blog.Post, posts)

ipsums = Table(
        'ipsum', metadata,
        Column('id', Integer, primary_key=True),
        Column('hash', String),
        Column('text', String))
mapper(generated.Ipsum, ipsums)

metadata.create_all(engine)
