from datetime import date
from unittest.mock import patch

from join_words import join_words
import unittest
import requests


def mocked_change(*args, **kwargs):
    return 'badger-racoon'


class TestJoinWords(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('A test suite begins')

    @classmethod
    def tearDownClass(cls):
        print('A test suite ends')

    def setUp(self):
        print('test starts')

    def tearDown(self):
        print('test ends')

    def test_join_words(self):
        result = join_words('Bada', 'boom')
        self.assertEqual(result, 'Bada - boom')

    @unittest.skip
    def test_skip(self):
        print('At the developers request')

    @unittest.skipIf(date.today().weekday() in [0, 2, 4], reason="Busy days")
    def test_by_days(self):
        print("Early testing saves time and money")

    @unittest.expectedFailure
    def expected_fail(self):
        result = join_words('Bada', 'boom')
        self.assertEqual(result, 'Big bada - boom')

    # =====================================================================

    @patch("requests.get", side_effect=mocked_change)
    def just_mock(self, mock):
        response = requests.get("https://www.google.com/search?q=badger/")
        self.assertEqual(response,'badger-racoon')
