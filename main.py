from models import Publisher, Book, Shop, Sale, Stock, create_tables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class Connect:
    DB_TYPE = os.getenv('DB_TYPE') or 'postgresql'
    DB_NAME = os.getenv('DB_NAME') or 'postgres'
    DB_USER = os.getenv('DB_USER') or 'postgres'
    DB_PASSWORD = os.getenv('DB_PASSWORD') or 'smog1718'
    DB_HOST = os.getenv('DB_HOST') or 'localhost'
    DB_PORT = os.getenv('DB_PORT') or 5432
    DSN = f'{DB_TYPE.lower()}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(DSN)
    Session = sessionmaker(bind=engine)()


def serching_publisher_name():
    query_join = session.query(Sale).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите имя издателя: ')
    query_result = query_join.filter(Publisher.publisher_name == query_publisher_name)
    for result in query_result.all():
        print(f'{result}')


def serching_publisher_id():
    publisher_id = input('Введите идентификатор издателя: ')
    query_join = session.query(Sale).join(Stock).join(Book).join(Publisher)
    
    for row in query_join.filter(Book.id_publisher == publisher_id):
        print(row)




if __name__ == '__main__':
    session = Connect.Session
    #serching_publisher_name()
    serching_publisher_id()
    session.close()
