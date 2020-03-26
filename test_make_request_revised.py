import unittest
from unittest.mock import patch
import make_request_revised
import requests


class Test_make_request_revised(unittest.TestCase):

    def test_build_url(self):
        self.assertEqual(make_request_revised.build_url("https://www.youtube.com/watch?v=6tNS--", "WetLI"),
                         "https://www.youtube.com/watch?v=6tNS--WetLI")
        self.assertEqual(make_request_revised.build_url(
            'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=', 2000),
                         "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=2000")

    def test_build_file_name(self):
        self.assertEqual(make_request_revised.build_file_name(2), "location_2")
        self.assertEqual(make_request_revised.build_file_name(54534), "location_54534")

    def test_make_request(self):
        with patch('requests.get') as mocked_get:
            url_base = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=1'
            header = {"token": "some_token", 'Content-Type': 'application/json'}
            make_request_revised.make_request(url=url_base, header=header)
        mocked_get.asserrt_called_once()

        expected_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=1"

        call_args = mocked_get.call_args[0][0]

        self.assertTrue(call_args, requests.codes.ok)
        self.assertEqual(expected_url, call_args)
        self.assertEqual("some_token", mocked_get.call_args[1]['headers']['token'])

    def test_create_file(self):
        pass


if __name__ == '__main__':
    unittest.main()
