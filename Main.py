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

# Объединение слева- направо
# shop_sample = session.query(Shop.name, Stock.id_book).join(Stock.shop).join(Sale).subquery()
#     # print(c)
# for res in session.query(Book.title, Publisher.name, Shop.name).join(Publisher).join(shop_sample, Book.id == shop_sample.c.id_book):
#     print(res)

# Объединение справа-налево
# subq = session.query(Shop.name, Stock.id).select_from(Shop).join(Stock).join(Sale).subquery()
# main_query = session.query(Book.title, Shop.name).select_from(Sale).\
#     join(Stock).join(Book).join(Publisher).join(subq, Sale.id_stock == Stock.id)
#
# for res in main_query:
#     print(res)
#
# print(subq)
# print(main_query)

query_result = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Publisher)\
    .join(Book).join(Stock).join(Sale).join(Shop).filter(Publisher.name == 'Пушкин')
for res in query_result:
    print(f'{res[0]} {res[1]} {res[2]} {res[3]}')