# TO RUN in Windows
# Run the following in the terminal without the hash sign:
# venv\Scripts\activate
# $env:FLASK_APP = "todo"
# $env:FLASK_ENV = "development"
# flask run -h localhost -p 3030

# TO RUN in MacOS/Linux
# Run the following in the terminal without the hash sign:
# . venv/bin/activate
# export FLASK_APP=todo
# export FLASK_ENV=development
# flask run -h localhost -p 3030

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask.json import jsonify


app = Flask(__name__)

# Sets the App config for SQL Alchemy with the database string
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/databasename'

# SQLAlchemy Instance
db = SQLAlchemy(app)


# Model for Task Table
class Task(db.Model):
    # Columns and Data Types should be the same as in the database
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False)
    content = db.Column(db.String(500), unique=False)
    is_deleted = db.Column(db.Boolean, default=False, unique=False)

    # Method to convert object to a dictionary
    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'is_deleted': self.is_deleted
        }
        return data

    # Method to populate object from a dictionary
    def from_dict(self, data):
        for field in ['title', 'content']:
            if field in data:
                setattr(self, field, data[field])


# API to get all tasks
@app.route('/api/task', methods=['GET'])
def get_tasks():
    result = []
    # .query came from the class inheriting (db.Model)
    # .all() will get all the tasks
    tasks = Task.query.all()
    for task in tasks:
        result.append(task.to_dict())
    # Will return a JSON format
    return jsonify(result)

# API to add a task
@app.route('/api/task', methods=['POST'])
def add_task():
    # request.get_json will get the JSON body from the requestt
    data = request.get_json() or {}

    if 'title' not in data and 'content' not in data:
        return jsonify({'message': 'Task must have at least title or content'})

    task = Task()
    task.from_dict(data)

    # Adds the record in the session
    db.session.add(task)
    # Save the changes to the database
    db.session.commit()

    return jsonify({'message': 'Task successfully added'})

# API to edit a task
@app.route('/api/task/<int:id>/edit', methods=['POST'])
def edit_task(id):
    data = request.get_json() or {}

    has_title_or_content = 'title' in data or 'content' in data

    if not has_title_or_content:
        return jsonify({'message': 'Task must have at least a title or content'})

    task = Task.query.get_or_404(id)

    # Updates the task
    if 'title' in data:
        task.title = data['title']
    if 'content' in data:
        task.content = data['content']

    if has_title_or_content:
        db.session.commit()

    return jsonify({'message': 'Task updated successfully'})

@app.route('/api/task/<int:id>/delete', methods=['POST'])
def delete_task(id):
    pass