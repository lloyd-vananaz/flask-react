from app import create_app, db
from app.tasks.models import Task


app = create_app(config_name='development', built_react_path='../../react-app/build')


# registers the function as a shell context function
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Task': Task}