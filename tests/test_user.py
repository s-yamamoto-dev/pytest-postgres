from src.model import Users
from src.session import create_session


def test_user():
    user_fields = {
        'name': 'テスト 太郎',
        'email': 'sample@example.com'
    }
    Users.create(user_fields)
    with create_session() as session:
        users = session.query(Users).all()
        assert len(users) == 1
