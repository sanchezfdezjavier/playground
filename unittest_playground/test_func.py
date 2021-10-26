from unittest import mock, TestCase

from google import call_google_api
import facebook


class TestApi(TestCase):

    @mock('call_google_api()', side_effect=[
        "data_1",
        "data_2",
        "data_3",
    ])
    def test_external_api(self):
        #self.assertEqual(google.call_google_api(), 'data_1')
        self.assertEqual(call_google_api(), 'data_1')
        self.assertEqual(call_google_api(), 'data_2')
        self.assertEqual(call_google_api(), 'data_3')
