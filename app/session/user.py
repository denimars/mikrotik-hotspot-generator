from sqlalchemy.orm import Session
from app.model.user import User

class UserSession:
    def __init__(self, db):
        self.db = db
    def create(self):
        try:
            with Session(self.db.connection_()) as session:
                user = User(id="1", nupy="tnest", password="12123", status=0)
                session.add(user)
                session.commit()
        except Exception as e:
            print(e)