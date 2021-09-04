from flask_script import Manager, Server
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand, upgrade
from app.models import *

app = create_app()
manager = Manager(app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)   # 创建数据库映射命令
manager.add_command('start', Server('0.0.0.0',port=9000, use_debugger=True))  # 创建启动命令


if __name__ == '__main__':
    manager.run()


