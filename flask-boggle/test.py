from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Always do this"""
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Makes sure correct information is in the session and html is displayed"""

        with self.client:
            response = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_valid_word(self):
        """Tests if a word is valid by modifying the board in the session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["M", "A", "T", "C", "H"], 
                                 ["M", "A", "T", "C", "H"], 
                                 ["M", "A", "T", "C", "H"], 
                                 ["M", "A", "T", "C", "H"], 
                                 ["M", "A", "T", "C", "H"]]
        response = self.client.get('/check-word?word=match')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Tests if the word is in the dictionary"""

        self.client.get('/')
        response = self.client.get('/check-word?word=impossible')
        self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Tests if that word checked from the dictionary is on the board"""

        self.client.get('/')
        response = self.client.get(
            '/check-word?word=pepepepepepepepepepppopopopoopopopopo')
        self.assertEqual(response.json['result'], 'not-word')

    

    # TODO -- write tests for every view function / feature!
