from app.database.db import DB
from app.model.declar import Base

db = DB(Base)
db.generate_table()