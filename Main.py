import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import config
import psycopg2

DSN = config.dsn_str
from models import create_tables, Course


engine = sq.create_engine(DSN)
create_tables(engine)
# delete_tables(engine)


# Session = sessionmaker(bind=engine)

# session = Session()
# session.add(course1)
# session.commit()
# print(course1)


