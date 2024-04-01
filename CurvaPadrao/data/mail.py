import unittest
from unittest.mock import patch
from authorization import Authorization

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        self.authorization = Authorization()

    @patch('authorization.requests.post')
    def test_create_user(self, mock_post):
        name = 'Jessica'
        email = 'email@email.com'
        password = 'Password@123'
        
        # Mock the response from the requests.post call
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'idToken': 'mocked_token'}

        # Call the method to test
        user_uid = self.authorization.create_user(name, email, password)

        # Assertions
        self.assertIsNotNone(user_uid)
        self.assertIsInstance(user_uid, str)
        self.assertTrue(mock_post.called)

if __name__ == '__main__':
    unittest.main()
