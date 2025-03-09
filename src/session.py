from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# MEMO: ローカルでのみ利用するため接続情報をハードコーディングしている
# 参考にする時は必ず外だしすること
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

def create_session():
    session = sessionmaker(engine)
    return session()
