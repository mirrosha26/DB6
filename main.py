from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale, create_tables
import sqlalchemy
import os


def info_book(session):
    request_in = input('Введите имя или id издателя: ')
    if request_in.isdigit():
        for data in session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.id == request_in).filter(Book.id_publisher == Publisher.id).filter(Stock.id_book == Book.id).filter(Shop.id == Stock.id_shop).filter(Sale.id_stock == Stock.id).all():
            print(f'{data.Book.title} | {data.Shop.name} | {data.Sale.price * data.Sale.count} | {data.Sale.date_sale}')
    else:
        for data in session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.name == request_in).filter(Book.id_publisher == Publisher.id).filter(Stock.id_book == Book.id).filter(Shop.id == Stock.id_shop).filter(Sale.id_stock == Stock.id).all():
            print(f'{data.Book.title} | {data.Shop.name} | {data.Sale.price * data.Sale.count} | {data.Sale.date_sale}')


if __name__ == '__main__':

    DB_TYPE = os.getenv('DB_TYPE') or 'postgresql'
    DB_NAME = os.getenv('DB_NAME') or 'test2'
    DB_USER = os.getenv('DB_USER') or 'postgres'
    DB_PASSWORD = os.getenv('DB_PASSWORD') or 'smog1718'
    DB_HOST = os.getenv('DB_HOST') or 'localhost'
    DB_PORT = os.getenv('DB_PORT') or 5432
    DSN = f'{DB_TYPE.lower()}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    engine = sqlalchemy.create_engine(DSN)
    #create_tables(engine)
    Session = sessionmaker(engine)
    session = Session()
    info_book(session)
    session.close()