import unittest

from muffin_rail._testrail_client import TestrailClient


class TestTestrailClient(unittest.TestCase):
    def test_init_error_handle(self):
        cases = [
            {
                "name": "no host",
                "test_data": {
                    "host": None,
                    "username": "abc",
                    "password": "abc",
                    "project_id": "123",
                    "suite_id": "123",
                },
            },
            {
                "name": "no username",
                "test_data": {
                    "host": "http://abc.com",
                    "username": None,
                    "password": "abc",
                    "project_id": "123",
                    "suite_id": "123",
                },
            },
            {
                "name": "no password",
                "test_data": {
                    "host": "http://abc.com",
                    "username": "abc",
                    "password": None,
                    "project_id": "123",
                    "suite_id": "123",
                },
            },
            {
                "name": "no project_id",
                "test_data": {
                    "host": "http://abc.com",
                    "username": "abc",
                    "password": "abc",
                    "project_id": None,
                    "suite_id": "123",
                },
            },
            {
                "name": "no suite_id",
                "test_data": {
                    "host": "http://abc.com",
                    "username": "abc",
                    "password": "abc",
                    "project_id": "123",
                    "suite_id": None,
                },
            },
        ]
        for case in cases:
            test_data = case["test_data"]
            with self.assertRaises(ValueError, msg=f"Case: {case['name']} - failed"):
                TestrailClient(
                    host=test_data["host"],
                    username=test_data["username"],
                    password=test_data["password"],
                    project_id=test_data["project_id"],
                    suite_id=test_data["suite_id"],
                ),
