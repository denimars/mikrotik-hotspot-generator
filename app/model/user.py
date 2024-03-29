from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import DateTime
from .declar import Base
   

class User(Base):
    __tablename__ = "user_acount"
    id:Mapped[str]  = mapped_column(String(255),primary_key=True)
    nupy:Mapped[str] = mapped_column(String(20))
    password:Mapped[str]=mapped_column(String(255))
    status:Mapped[bool] = mapped_column()
    created_at:Mapped[str] = mapped_column(DateTime)

    def __repr__(self) -> str:
      return f"User(id={self.id!r}, nupy={self.nupy!r}, password={self.password!r}, status={self.status!r}, created_at={self.created_at!r})"