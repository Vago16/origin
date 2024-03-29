"""Message View tests."""

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_message_views.py


import os
from unittest import TestCase

from models import db, connect_db, Message, User

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app, CURR_USER_KEY

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


class MessageViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)
        self.testuser2 = User.signup(
            username = "testuser2",
            email = "other@test.com",
            password = "testuser2",
            image_url = None
        )

        db.session.commit()

    def tearDown(self):
        retval = super().tearDown()
        db.session.rollback()
        return retval

        db.session.commit()

    def test_add_message(self):
        """Can use add a message?"""

        # Since we need to change the session to mimic logging in,
        # we need to use the changing-session trick:

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            # Now, that session setting is saved, so we can have
            # the rest of ours test

            resp = c.post("/messages/new", data={"text": "Hello"})

            # Make sure it redirects
            self.assertEqual(resp.status_code, 302)

            msg = Message.query.one()
            self.assertEqual(msg.text, "Hello")

    def test_message_show(self):
        """Does adding a new message create a new page?"""

        message = Message(id=0xf00f, text="Hello world", user_id=self.testuser.id)
        db.session.add(message)
        db.session.commit()

        with self.client as c:
            with c.session_transaction() as session:
                session[CURR_USER_KEY] = self.testuser.id
            
            response = c.get(f'/messages/{0xf00f}')

            self.assertEqual(response.status_code, 200)
            self.assertIn("Hello world", str(response.data))
    
    def test_logged_out_message_add(self):
        """Is a message addition rejected when not logged in?"""

        with self.client as c:
            response = c.post("/messages/new", data={"text": "Hello"}, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("Access unauthorized", str(response.data))

    def test_invalid_user_message_add(self):
        """Is a message addition rejected with an invalid user ID?"""

        with self.client as c:
            with c.session_transaction() as session:
                session[CURR_USER_KEY] = 0xdeadbeef
            
            response = c.post("/messages/new", data={"text": "Hello"}, follow_redirects=True)
            
            self.assertEqual(response.status_code, 200)
            self.assertIn("Access unauthorized", str(response.data))

    def test_invalid_message_show(self):
        """Does showing an invalid message ID get rejected?"""

        with self.client as c:
            with c.session_transaction() as session:
                session[CURR_USER_KEY] = self.testuser.id
            
            response = c.get("/messages/12345678", follow_redirects=True)

            self.assertEqual(response.status_code, 404)

 
