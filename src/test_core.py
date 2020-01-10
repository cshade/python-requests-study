import unittest
from core import get_poem
from requests.exceptions import HTTPError
from unittest.mock import patch

class BasicTests(unittest.TestCase):
    @patch('core.requests.get')
    def test_request_response(self, mock_get):
        mock_get.return_value.status_code = 200
        response = get_poem('https://cagibilit.com/wp-json/wp/v2/posts/10555')

        # Assert that the request-response cycle completed successfully with status code 200.
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
