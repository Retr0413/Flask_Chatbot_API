import unittest
from app import create_app

class ChatbotTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_chatbot_response(self):
        response = self.client.post('/chatbot', json={'massage': 'Hello'})
        json_data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', json_data)
        self.assertEqual(json_data['response'], 'Hello How can I assist you today')

if __name__ == "__main__":
    unittest.main()