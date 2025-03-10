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
        with create_session() as session:
            session.add(user)
            session.commit()
        return user

    @classmethod
    def update(cls, user_id, name):
        with create_session() as session:
            user = session.query(Users).get(user_id)
            user.name = name
            session.commit()

    @classmethod
    def list(cls):
        with create_session() as session:
            users = session.query(Users).all()
            return users

    @classmethod
    def delete(cls, user_id):
        with create_session() as session:
            user = session.query(Users).get(user_id)
            session.delete(user)
            session.commit()
