from sqlalchemy.orm import Session
from app.model.user import User
from uuid import uuid4
from datetime import datetime
from sqlalchemy import select, update, bindparam
import requests
import json

class UserSession:
    def __init__(self, db):
        self.db = db
    def create(self):
        try:
            with Session(self.db.connection_()) as session:
                user = User(id=str(uuid4()), nupy="tnest", password="12123", status=0, created_at=datetime.now())
                session.add(user)
                session.commit()
                session.close()
        except Exception as e:
            print(e)
    
    def read(self):
        statement = select(User).where(User.status==0)
        data = None
        with Session(self.db.connection_()) as session:
            data = session.execute(statement).all()
        session.close()
        return data
    def get_data_from_server(self):
        request = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        print(request.status_code)
        data =  json.loads(request.content)
        print(data["userId"])
        print(data["id"])
    
    def update(self):
        getuser = self.read()
        with Session(self.db.connection_()) as session:
          for user in getuser:
                statement  = update(User).where(User.id==user[0].id).values(status=True)
                session.execute(statement)
                session.commit()
        session.close()

