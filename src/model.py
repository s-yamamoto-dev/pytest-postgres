from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

from src.session import create_session

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))

    @classmethod
    def create(cls, *args, **kwargs):
        user = Users(**kwargs)
        session = create_session()
        with create_session() as session:
            session.add(user)
            session.commit()
        return user
