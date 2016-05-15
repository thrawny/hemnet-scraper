from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from . import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_hemnet_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class HemnetItem(DeclarativeBase):
    __tablename__ = "hemnet_items"

    id = Column(Integer, primary_key=True)

    hemnet_id = Column('hemnet_id', Integer, index=True)

    url = Column('url', String)

    broker_name = Column('broker_name', String, default='')
    broker_phone = Column('broker_phone', String, default='')
    broker_email = Column('broker_email', String, default='')

    broker_firm = Column('broker_firm', String, default='')
    broker_firm_phone = Column('broker_firm_phone', String, default='')

    sold_date = Column('sold_date', Date, nullable=True)

    price_per_square_meter = Column('price_per_square_meter', Float, nullable=True)
    price = Column('price', Integer, nullable=True)
    asked_price = Column('asked_price', Integer, nullable=True)
    price_trend_flat = Column('price_trend_flat', Integer, nullable=True)
    price_trend_percentage = Column('price_trend_percentage', Integer, nullable=True)

    rooms = Column('rooms', Float, nullable=True)
    monthly_fee = Column('monthly_fee', Integer, nullable=True)
    square_meters = Column('square_meters', Float, nullable=True)
    cost_per_year = Column('cost_per_year', Integer, nullable=True)
    year = Column('year', String, default='')
    type = Column('type', String, default='')

    address = Column('address', String, default='')
    geographic_area = Column('geographic_area', String, default='')
