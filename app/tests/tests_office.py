

import unittest
import json
import base64

from app import create_app


class TestPoliticoOffices(unittest.TestCase):

    def setUp(self):
        """ Test runner will run this method before each test """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        """ This will be invoked after each test has been completed. """
        self.app_context.pop()

        """ Tests for political offices endpoints 

        POST /offices
        GET /offices
        GET /offices/<office-id>
        """

    def testCreateOffice(self):
        """ Tests creating a new office """
        test_office = {
            "type": "Presidential",
            "name": "President"
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})
        return test_results

    def testOfficeValidity(self):
        """ Tests if all information regarding the office is captured """
        test_office = {
            "type": "Presidential"
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 406)

    def testOfficeNameValidity(self):
        """ Tests Office Name Validity """
        test_office = {
            "type": "Presidential",
            "name": ""
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 406)

    def testOfficeTypeValidity(self):
        """ Tests Office Type Validity """
        test_office = {
            "type": "",
            "name": "President"
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 406)

    def testGetAlloffices(self):
        """ Tests fetches all offices created """

        test_offices = {1:
                        {
                            "type": "Presidential",
                            "name": "President"
                        }
                        }

        test_results = self.client.get("api/v1/offices", data=json.dumps(
            test_offices), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 200)

    def testGetSpecificOffice(self):
        """ Tests fetch specific party """

        test_offices = {1:
                        {
                            "type": "Presidential",
                            "name": "President"
                        }
                        }

        test_results = self.client.get("api/v1/offices/1", data=json.dumps(
            test_offices), headers={'content-type': 'application/json'})
        test_fail_results = self.client.get("api/v1/offices/2", data=json.dumps(
            test_offices), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 200)
        self.assertEqual(test_fail_results.status_code, 404)
