import unittest
import requests
from test.base import BASE_URL



class UrlTest(unittest.TestCase):
    def test_shounitrt_url(self):
        url = BASE_URL + '/short_url'
        data = {
            'url': 'http://coolpython.net'
        }

        res = requests.post(url, json=data)
        print(res.text)
