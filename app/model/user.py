from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import DeclarativeBase
from .declar import Base
   

class User(Base):
    __tablename__ = "user_acount"
    id:Mapped[str]  = mapped_column(String(255),primary_key=True)
    nupy:Mapped[str] = mapped_column(String(20))
    password:Mapped[str]=mapped_column(String(255))

    def __repr__(self) -> str:
      return f"User(id={self.id!r}, name={self.nupy!r}, fullname={self.password!r})"