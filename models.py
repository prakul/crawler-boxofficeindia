from sqlalchemy import create_engine,Column,Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    print URL(**settings.DATABASE)
    return create_engine(URL(**settings.DATABASE))

def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)
    
    
class Movies(DeclarativeBase):
    __tablename__="movies"
    id = Column(Integer,primary_key=True)
    title = Column('title',String)
    rel_date = Column('rel_date',String)
    genre = Column('genre',String)
    run_time = Column('run_time',String)
    budget = Column('budget',String)
    screens = Column('screens',String)
    footfalls = Column('footfalls',String)
    dis_share = Column('dis_share',String)
    total_gross = Column('total_gross',String)
    total_nett_gross = Column('total_nett_gross',String)
    link = Column('link',String)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    