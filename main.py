from flask_script import Manager
from app.main import create_app, init_db_sqlite
from app.main.controller import user_controller

app = create_app('dev')

manager = Manager(app)


@manager.command
def run():
    app.register_blueprint(user_controller.bp)
    app.run()


@manager.command
def init_db():
    init_db_sqlite(app)


if __name__ == '__main__':
    manager.run()
