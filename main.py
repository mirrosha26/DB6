from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale, create_tables
import json
import sqlalchemy
import os

def connect():
    DB_TYPE = os.getenv('DB_TYPE') or 'postgresql'
    DB_NAME = os.getenv('DB_NAME') or 'test2'
    DB_USER = os.getenv('DB_USER') or 'postgres'
    DB_PASSWORD = os.getenv('DB_PASSWORD') or 'smog1718'
    DB_HOST = os.getenv('DB_HOST') or 'localhost'
    DB_PORT = os.getenv('DB_PORT') or 5432
    DSN = f'{DB_TYPE.lower()}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    return sqlalchemy.create_engine(DSN)

    with open('tests_data.json', 'r') as f:
        data = json.load(f)
        Session = sessionmaker(engine)
        session = Session()
        for element in data:
            if element['model'] == 'publisher':
                instance = Publisher(name=element['fields']['name'])
                session.add(instance)
                session.commit()
            elif element['model'] == 'book':
                instance = Book(title=element['fields']['title'], id_publisher=element['fields']['id_publisher'])
                session.add(instance)
                session.commit()
            elif element['model'] == 'shop':
                instance = Shop(name=element['fields']['name'])
                session.add(instance)
                session.commit()
            elif element['model'] == 'stock':
                instance = Stock(id_book=element['fields']['id_book'], id_shop=element['fields']['id_shop'], count=element['fields']['count'])
                session.add(instance)
                session.commit()
            elif element['model'] == 'sale':
                instance = Sale(price=element['fields']['price'], date_sale=element['fields']['date_sale'], count=element['fields']['count'], id_stock=element['fields']['id_stock'])
                session.add(instance)
                session.commit()
        session.close()

def info_book():
    request_in = input('Введите имя или id издателя: ')
    if request_in.isdigit():
        for data in session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.id == request_in).filter(Book.id_publisher == Publisher.id).filter(Stock.id_book == Book.id).filter(Shop.id == Stock.id_shop).filter(Sale.id_stock == Stock.id).all():
            print(f'{data.Book.title} | {data.Shop.name} | {data.Sale.price * data.Sale.count} | {data.Sale.date_sale}')
    else:
        for data in session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.name == request_in).filter(Book.id_publisher == Publisher.id).filter(Stock.id_book == Book.id).filter(Shop.id == Stock.id_shop).filter(Sale.id_stock == Stock.id).all():
            print(f'{data.Book.title} | {data.Shop.name} | {data.Sale.price * data.Sale.count} | {data.Sale.date_sale}')


if __name__ == '__main__':
    engine = connect()

    create_tables(engine)

    Session = sessionmaker(engine)
    session = Session()
    info_book()
    session.close()

    
