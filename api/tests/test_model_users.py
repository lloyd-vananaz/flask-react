import unittest

from app import create_app
from app.core import db
from app.users.models import User


class TestModelUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_insert_user(self):
        username = 'test01'

        # Create user since we are using an empty temporary database
        user = User(username=username, email='test@test.com')
        db.session.add(user)
        db.session.commit()

        # Get user from database
        user_from_db = User.query.filter_by(username=username).first()

        self.assertEqual(user, user_from_db)

    def test_password_setter(self):
        user = User(username='test01')
        user.set_password('Cat')
        self.assertTrue(user.password_hash is not None)