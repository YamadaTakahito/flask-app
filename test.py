import unittest
import main


class TestPing(unittest.TestCase):
    def test_ping(self):
        self.assertEqual(main.ping(), 'pong')


if __name__ == '__main__':
    unittest.main()