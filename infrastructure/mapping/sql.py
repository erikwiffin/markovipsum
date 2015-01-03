from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, mapper

from domain.model import blog

engine = create_engine('postgresql://postgres:password@localhost/markovipsum', echo=True)
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

posts.drop(engine)
metadata.create_all(engine)
