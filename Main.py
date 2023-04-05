import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import config
import psycopg2
import json
from models import create_tables, Publisher, Book, Sale, Shop, Stock

# requested_publisher = input('Введите автора / издательство: ')

DSN = config.dsn_str

engine = sq.create_engine(DSN)
# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# if requested_publisher ==
shop_sample = session.query(Shop.name, Stock.id_book).join(Stock.shop).join(Sale).subquery()
    # print(c)
for res in session.query(Book.title, Publisher.name, Shop.name).join(Publisher).join(shop_sample, Book.id == shop_sample.c.id_book):
    print(res)