import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from app.model.user import User
from dotenv import load_dotenv
import os

load_dotenv()
class DB():
    def __init__(self, declarative):
        self.engine = db.create_engine("mysql+pymysql://"+os.getenv("HOTSPOT_USER")+":"+os.getenv("HOTSPOT_PASSWORD")+"@"+os.getenv("HOTSPOT_HOST")+"/"+os.getenv("HOTSPOT_DB"))
        self.connection = self.engine.connect()
        self.declarative = declarative
    
    def generate_table(self):
        self.declarative.metadata.create_all(self.engine)



# if __name__=='__main__':
#     # Base = declarative_base()
#     db = DB(Base)
#     db.generate_table()