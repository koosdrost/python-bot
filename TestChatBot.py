import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
import json
import requests
import bot

class TestChatbot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        setup flask test client
        """
        bot.app.testing = True
        cls.app = bot.app.test_client()

    def test_bot_quote(self):
        """
        Test bot returns quote
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value = MagicMock(status_code=200)
            mock_get.return_value.json.return_value = {"content": "Test quote", "author": "Test author"}
            response = self.app.post('/', data=json.dumps({"Body": "quote"}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Test quote (Test author)</Message></Response>')

    def test_bot_quote_fail(self):
        """
        Test bot returns quote failure message
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value = MagicMock(status_code=404)
            response = self.app.post('/', data=json.dumps({"Body": "quote"}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Ik kan geen quotes vinden op dit moment</Message></Response>')

    def test_bot_http(self):
        """
        Test bot returns http cat pic
        """
        with patch('requests.get') as mock_get:
            response = self.app.post('/', data=json.dumps({"Body": "http 200"}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Media>https://http.cat/200</Media></Message></Response>')

    def test_bot_vacatures(self):
        """
        Test bot returns vacatures
        """
        with patch('urllib.request.urlopen') as mock_get:
            mock_get.return_value = MagicMock()
            mock_get.return_value.read.return_value = '<div class="elementor-button-wrapper"><a href="/test-job"></a></div>'
            response = self.app.post('/', data=json.dumps({"Body": "vacatures"}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Alle huidige vacatures bij Conspect</Message><Message>https://conspect.nl/test-job</Message></Response>')

    def test_bot_wiki(self):
        """
        Test bot returns wiki page
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value = MagicMock(status_code=200)
            mock_get.return_value.url = 'https://nl.wikipedia.org/wiki/Test_page'
            response = self.app.post('/', data=json.dumps({"Body": "wiki Test_page"}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_data(as_text=True), '<?xml version="1.0" encoding="UTF-8"?><Response><Message>https://nl.wikipedia.org/wiki/Test_page</Message></Response>')

    def test_bot_cat(self):
        """
        Test bot returns cat pic
        """
        response = self.app.post('/', data=json.dumps({"Body": "cat"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('https://cataas.com/cat', response.get_data(as_text=True))
