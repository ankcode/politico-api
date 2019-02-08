import unittest
import json
import base64

from app import create_app


class TestPolitico(unittest.TestCase):

    def setUp(self):
        """ Test runner will run this method before each test """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        """ This will be invoked after each test has been completed. """
        self.app_context.pop()

    def testCreateParty(self):
        """ Tests creating a new party"""
        test_party = {
            "id": "1",
            "name": "CCM",
            "hqAddress": "Nairobi Kenya",
            "logourl": "party.jpg"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers={
                                        'content-type': 'application/json', 'Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})
        return test_results

    def testInformationValidity(self):
        """ Tests if all information is captured """
        test_party = {
            "id": "1",
            "name": "CCM",
            "hqAddress": "Nairobi Kenya"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers={
                                        'content-type': 'application/json', 'Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})

        self.assertEqual(test_results.status_code, 406)

    def testIDValidity(self):
        """ Tests ID validity """
        test_party = {
            "id": "",
            "name": "CCM",
            "hqAddress": "Nairobi Kenya",
            "logourl": "party.jpg"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers={
                                        'content-type': 'application/json', 'Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})

        self.assertEqual(test_results.status_code, 406)

    def testNameValidity(self):
        """ Tests Name Validity """
        test_party = {
            "id": "1",
            "name": "",
            "hqAddress": "Nairobi Kenya",
            "logourl": "party.jpg"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers={
                                        'content-type': 'application/json', 'Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})

        self.assertEqual(test_results.status_code, 406)

    def testAddressValidity(self):
        """ Tests Address Validity """
        test_party = {
            "id": "1",
            "name": "CCM",
            "hqAddress": "",
            "logourl": "party.jpg"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers={
                                        'content-type': 'application/json', 'Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})

        self.assertEqual(test_results.status_code, 406)

    def testURLValidity(self):
        """ Tests URL Validity """
        test_party = {
            "id": "1",
            "name": "CCM",
            "hqAddress": "Nairobi Kenya",
            "logourl": ""
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers={
                                        'content-type': 'application/json', 'Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})

        self.assertEqual(test_results.status_code, 406)

    def testGetAllParties(self):
        """ Tests fetch all parties """

        test_political_parties = [
            {
                "id": "1",
                "name": "CCM",
                "hqAddress": "Nairobi Kenya",
                "logourl": "party.jpg"
            }
        ]

        test_results = self.client.get("api/v1/parties", data=json.dumps(
            test_political_parties), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 200)

    def testGetSpecificParty(self):
        """ Tests fetch specific party """

        test_political_parties = [
            {
                "id": "1",
                "name": "CCM",
                "hqAddress": "Nairobi Kenya",
                "logourl": "party.jpg"
            }
        ]

        test_results = self.client.get("api/v1/parties/1", data=json.dumps(
            test_political_parties), headers={'content-type': 'application/json'})
        test_fail_results = self.client.get("api/v1/parties/2", data=json.dumps(
            test_political_parties), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 200)
        self.assertEqual(test_fail_results.status_code, 404)

    def testDeleteSpecificParty(self):
        """ Tests deletes specific party """

        test_political_parties = [
            {
                "id": "1",
                "name": "CCM",
                "hqAddress": "Nairobi Kenya",
                "logourl": "party.jpg"
            },
            {
                "id": "2",
                "name": "TNA",
                "hqAddress": "Nairobi Kenya",
                "logourl": "party.jpg"
            }
        ]

        test_results = self.client.get("api/v1/parties/1", data=json.dumps(
            test_political_parties), headers={'content-type': 'application/json'})
        test_fail_results = self.client.get("api/v1/parties/3", data=json.dumps(
            test_political_parties), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 200)
        self.assertEqual(test_fail_results.status_code, 404)

        """ Tests for political offices endpoints 

            POST /offices
            GET  /offices
            GET  /offices/<office-id>
        
        """

    def testCreateOffice(self):
        """ Tests creating a new office """
        test_office = {
            "id": "1",
            "type": "Presidential",
            "name": "President"
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})
        return test_results

    def testOfficeValidity(self):
        """ Tests if all information regarding the office is captured """
        test_office = {
            "id": "1",
            "type": "Presidential",
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 406)

    def testOfficeIDValidity(self):
        """ Tests Office ID validity """
        test_office = {
            "id": "",
            "type": "Presidential",
            "name": "President"
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 406)

    def testOfficeNameValidity(self):
        """ Tests Office Name Validity """
        test_office = {
            "id": "1",
            "type": "Presidential",
            "name": ""
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 406)

    def testOfficeTypeValidity(self):
        """ Tests Office Type Validity """
        test_office = {
            "id": "1",
            "type": "",
            "name": "President"
        }

        test_results = self.client.post(
            "api/v1/offices", data=json.dumps(test_office), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 406)

    def testGetAlloffices(self):
        """ Tests fetches all offices created """

        test_offices = [
            {
                "id": "1",
                "type": "Presidential",
                "name": "President"
            }
        ]

        test_results = self.client.get("api/v1/offices", data=json.dumps(
            test_offices), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 200)

    
    def testGetSpecificOffice(self):
        """ Tests fetch specific party """

        test_offices = [
            {
                "id": "1",
                "type": "Presidential",
                "name": "President"
            }
        ]

        test_results = self.client.get("api/v1/parties/1", data=json.dumps(
            test_offices), headers={'content-type': 'application/json'})
        test_fail_results = self.client.get("api/v1/parties/2", data=json.dumps(
            test_offices), headers={'content-type': 'application/json'})

        self.assertEqual(test_results.status_code, 200)
        self.assertEqual(test_fail_results.status_code, 404)
