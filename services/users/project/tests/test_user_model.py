import unittest

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase

from sqlalchemy.exc import IntegrityError


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return user


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('test', 'test@test.com', 'thisisapassword')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)
        self.assertTrue(user.password)

    def test_add_user_duplicate_username(self):
        user = User(
            username='test',
            email='test@test.com',
            password='thisisapassword',
        )
        db.session.add(user)
        db.session.commit()
        duplicate_user = User(
            username='test',
            email='dup_test@test.com',
            password='thisisapassword',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        user = User(
            username='test',
            email='test@test.com',
            password='thisisapassword',
        )
        db.session.add(user)
        db.session.commit()
        duplicate_user = User(
            username='dup_test',
            email='test@test.com',
            password='thisisapassword',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = User(
            username='test',
            email='test@test.com',
            password='thisisapassword',
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_password_are_random(self):
        user_one = add_user('khanh', 'khanhnguyen@gmail.com', 'password')
        user_two = add_user('thu', 'thuhoang@gmail.com', 'password')
        self.assertNotEqual(user_one.password, user_two.password)


if __name__ == '__main__':
    unittest.main()
