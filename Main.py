import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import config
import psycopg2
import json
from models import create_tables, Publisher, Book, Sale, Shop, Stock

DSN = config.dsn_str

engine = sq.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()