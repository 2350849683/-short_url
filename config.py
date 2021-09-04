class Config():
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:6606/testDB?charset=utf8"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SECRET_KEY = 'secret key to protect from csrf'


    @staticmethod
    def init_app(app):
        pass