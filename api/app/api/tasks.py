from flask import request, Response
from flask.json import jsonify
from flask_cors.decorator import cross_origin
from app import db
from app.api import bp
from app.models import Task
from app.api.errors import bad_request


@bp.route('/task', methods=['GET'])
@cross_origin()
def get_tasks():
    result = []
    tasks = Task.query.filter_by(is_deleted=False).all()
    for task in tasks:
        result.append(task.to_dict())
    return jsonify(result)

@bp.route('/task', methods=['POST'])
@cross_origin()
def add_task():
    data = request.get_json() or {}

    if 'title' not in data and 'content' not in data:
        return bad_request('Task must have at least a title or content')

    task = Task()
    task.from_dict(data)
    
    db.session.add(task)
    db.session.commit()

    return Response(status=201)

@bp.route('/task/<int:id>', methods=['GET'])
@cross_origin()
def get_task_by_id(id):
    result = Task.query.get_or_404(id)
    return jsonify(result.to_dict())

@bp.route('/task/<int:id>/edit', methods=['POST'])
@cross_origin()
def edit_task_by_id(id):
    data = request.get_json() or {}

    has_title_or_content = 'title' in data or 'content' in data

    if not has_title_or_content:
        return bad_request('Task must have at least a title or content')

    task = Task.query.get_or_404(id)
    
    if 'title' in data:
        task.title = data['title']
    if 'content' in data:
        task.content = data['content']

    if has_title_or_content:
        db.session.commit()

    return Response(status=201)

@bp.route('/task/<int:id>/delete', methods=['POST'])
@cross_origin()
def delete_task_by_id(id):
    task = Task.query.get_or_404(id)
    
    # this will delete the record
    # db.session.delete(task)
    # db.session.commit()

    # this will just update the is_deleted column
    task.is_deleted = True
    db.session.commit()

    return Response(status=201)