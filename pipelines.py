# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker 
from models import Movies,db_connect,create_deals_table
import json

class boxOfficePipeline(object):
    def __init__(self):
        self.file = open('dump1.jl','wb')
        engine = db_connect()
        
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)
    
    def process_item(self, item, spider):
        
        line = json.dumps(dict(item))+"\n"
        self.file.write(line)
        
        session = self.Session()
        movie = Movies(**item)
        
        try:
            session.add(movie)
            print 'successfully added'
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item




















