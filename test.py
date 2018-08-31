import unittest

import requests


class TestPing(unittest.TestCase):
    def test_ping(self):
        self.assertEqual(requests.get('http://localhost:8000/ping').content, b'pong')

if __name__ == '__main__':
    unittest.main()