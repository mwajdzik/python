# https://realpython.com/python-mock-library/

from unittest.mock import Mock

# Create a mock object
json = Mock()
json.loads('{"key": "value"}')

json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')

print(json.loads.call_count)
print(json.loads.call_args)
print(json.loads.call_args_list)
print(json.method_calls)

json.loads('{"key": "value"}')

# ---

import datetime
from unittest.mock import Mock

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

print(tuesday)
print(saturday)

datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


datetime.datetime.today.return_value = tuesday
assert is_weekday()

datetime.datetime.today.return_value = saturday
assert not is_weekday()

# ---

import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()

    return None


class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        requests.get.side_effect = Timeout

        with self.assertRaises(Timeout):
            get_holidays()

# ---

import requests
import unittest
from unittest.mock import Mock

requests = Mock()


def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()

    return None


class TestCalendar(unittest.TestCase):
    def log_request(self, url):
        print(f'Making a request to {url}.')
        print('Request received!')

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock

    def test_get_holidays_logging(self):
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'


if __name__ == '__main__':
    unittest.main()
