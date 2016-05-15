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

    hemnet_id = Column(Integer, index=True)

    url = Column(String)

    broker_name = Column(String, default='')
    broker_phone = Column(String, default='')
    broker_email = Column(String, default='', index=True)

    broker_firm = Column(String, default='')
    broker_firm_phone = Column(String, default='')

    sold_date = Column(Date, nullable=True)

    price_per_square_meter = Column(Float, nullable=True)
    price = Column(Integer, nullable=True)
    asked_price = Column(Integer, nullable=True)
    price_trend_flat = Column(Integer, nullable=True)
    price_trend_percentage = Column(Integer, nullable=True)

    rooms = Column(Float, nullable=True)
    monthly_fee = Column(Integer, nullable=True)
    square_meters = Column(Float, nullable=True)
    cost_per_year = Column(Integer, nullable=True)
    year = Column(String, default='')
    type = Column(String, default='')

    address = Column(String, default='')
    geographic_area = Column(String, default='')
