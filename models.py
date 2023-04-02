import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
# from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=48), unique=True)
    def __str__(self):
        return f'{self.id} : {self.name}'

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=48), unique=True)
    id_publisher = jhj

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

