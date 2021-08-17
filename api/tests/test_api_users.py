import unittest
import json

from app import create_app
from app.core import db
from app.users.models import User


class TestModelUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_api(self):
        # Dummy data
        username = 'test02'
        password = 'testing12341234'
        user = User(username=username, email='test@test.com')

        # Call register API
        response = self.client.post(
            '/api/user/register',
            json = {
                'username': user.username,
                'email': user.email,
                'password': password,
                'password2': password
            }
        )
        json_response = json.loads(response.get_data(as_text=True))

        # Get user from database
        user_from_db = User.query.filter_by(username=username).first()

        self.assertEqual(json_response['message'], 'Registration successfull')
        self.assertEqual(user.username, user_from_db.username)
        self.assertEqual(user.email, user_from_db.email)
        self.assertTrue(user_from_db.check_password(password))