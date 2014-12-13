from flask.ext.script import Manager

from app import app


manager = Manager(app)

@manager.command
def start_dev():
    app.run(debug=True)


@manage.command
def start_proud():
    app.run(debug=False)

if __name__ == "__main__":
    manager.run()