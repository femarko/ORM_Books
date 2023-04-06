import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import config
import psycopg2
from models import create_tables, Publisher, Book, Sale, Shop, Stock


DSN = config.dsn_str
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

requested_publisher = input('Введите автора / издательство: ')
query_result = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Publisher)\
    .join(Book).join(Stock).join(Sale).join(Shop).filter(Publisher.name == requested_publisher)

for res in query_result:
    print(f'{res[0]}\t{res[1]}\t{res[2]}\t{res[3]}')
