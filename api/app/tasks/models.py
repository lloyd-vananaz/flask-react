from app.core import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True, unique=False)
    content = db.Column(db.String(500), index=True, unique=False)
    is_deleted = db.Column(db.Boolean, index=True, default=False, unique=False)

    def __repr__(self):
        return '<Task {}>'.format(self.title)

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'is_deleted': self.is_deleted
        }
        return data

    def from_dict(self, data):
        for field in ['title', 'content']:
            if field in data:
                setattr(self, field, data[field])
            