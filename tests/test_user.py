from src.model import Users
from src.session import create_session


def test_user_create():
    user_fields = {
        'name': 'テスト 太郎',
        'email': 'sample@example.com'
    }
    Users.create(user_fields)
    with create_session() as session:
        users = session.query(Users).all()
        assert len(users) == 1

def test_user_list():
    with create_session() as session:
        user = Users(name='sample', email='sample@example.com')
        session.add(user)
        session.commit()
    users = Users.list()
    assert len(users) == 1

def test_user_update():
    with create_session() as session:
        user = Users(name='sample', email='sample@example.com')
        session.add(user)
        session.commit()
        Users.update(user_id=user.id, name='changed')

    with create_session() as session:
       assert session.query(Users).get(user.id).name == 'changed'

def test_user_delete():
    with create_session() as session:
        user = Users(name='sample', email='sample@example.com')
        session.add(user)
        session.commit()
        Users.delete(user_id=user.id)

    with create_session() as session:
       assert session.query(Users).get(user.id) == None
