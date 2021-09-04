from app import db
from sqlalchemy import Integer, String, Boolean
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    username = db.Column(String(50), nullable=False)                # 用户名
    password = db.Column(String(100), nullable=False)                # 密码
    email = db.Column(String(50), nullable=False)                   # 邮箱
    is_admin = db.Column(Boolean, nullable=False, default=False)    # 是否管理员
    surplus = db.Column(Integer, nullable=False, default=0)         # 剩余调用次数

    @classmethod
    def add_admin(cls):
        user = User(username='admin', password=generate_password_hash('123456'), email='xigongda2000608@163.com')
        db.session.add(user)
        db.session.commit()
# 定义User对象, 尽量展示一些创建选项:
class url(db.Model):
    # 表的名字:
    __tablename__ = 'url'
    # 创建表的扩展设置，这里设置表的字符集为utf8
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    short_url = db.Column(String(1000))
    long_url = db.Column(String(100))
class url_index(db.Model):
    # 表的名字:
    __tablename__ = 'url_index'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    index=db.Column(Integer)

