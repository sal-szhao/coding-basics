import unittest

from messageboard import app, db
from messageboard.models import Message
from messageboard.forms import MessageForm
from messageboard.commands import forge, initdb

from flask import abort

class MessageboardTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )

        app.config["WTF_CSRF_ENABLED"] = False

        db.create_all()

        # user = User(name='Test', username='test')
        # user.set_password('123') 
        # movie = Movie(title='Test Movie Title', year='2019')


        # db.session.add_all([user, movie])
        # db.session.commit()

        self.client = app.test_client()
        self.runner = app.test_cli_runner()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        self.assertIsNotNone(app)
    
    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_404_page(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertIn('Page Not Found - 404', data)
        self.assertIn('Go Back', data)
        self.assertEqual(response.status_code, 404)

    def test_500_page(self):
        @app.route('/500')
        def throw_500_error():
            abort(500)

        response = self.client.get('/500')
        data = response.get_data(as_text=True)
        self.assertIn('Internal Server Error', data)
        self.assertIn('Go Back', data)
        self.assertEqual(response.status_code, 500)

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('Say Hello', data)
        self.assertIn('Name', data)
        self.assertIn(u'天王盖地虎', data)
        self.assertIn('Submit', data)
        self.assertIn('0 messages', data)
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        response = self.client.post('/', data=dict(
            name='New User',
            message='greeting',
            password=u'宝塔镇河妖'
        ), follow_redirects=True)

        data = response.get_data(as_text=True)
        self.assertIn('New User', data)
        self.assertIn('greeting', data)
        self.assertIn('Your message have been sent to the world!', data)

    def test_form_validate(self):
        response = self.client.post('/', data=dict(
            name='New Userasdfasdfasdfasdasdsadf',
            message='greeting',
            password=u'宝塔镇河妖1'
        ), follow_redirects=True)
        
        data = response.get_data(as_text=True)
        self.assertIn('The captcha value must be', data)
        self.assertIn('Field must be between 1 and 20 characters long.', data)

        response = self.client.post('/', data=dict(
            name='',
            message='2019'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('This field is required.', data)

        response = self.client.post('/', data=dict(
            name='abcabc',
            message=''
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('This field is required.', data)

    def test_forge_command(self):
        result = self.runner.invoke(forge)
        self.assertIn('faked messages.', result.output)
        self.assertEqual(Message.query.count(), 20)

    def test_forge_command_count(self):
        result = self.runner.invoke(forge, ['--count', '40'])
        self.assertIn('faked messages.', result.output)
        self.assertEqual(Message.query.count(), 40)

    def test_initdb_command(self):
        result = self.runner.invoke(initdb)
        self.assertIn('Initialized database.', result.output)


if __name__ == '__main__':
    unittest.main()