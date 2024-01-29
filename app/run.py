from app.database.db import DB
from app.model.declar import Base
from app.session.user import UserSession

db = DB(Base)
db.generate_table()
user = UserSession(db)
# user.read()
user.update()

user.create()
user.get_data_from_server()

