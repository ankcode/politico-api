import unittest, json, base64

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
            "id":"1",
            "name":"CCM",
            "hqAddress":"Nairobi Kenya",
            "logourl":"party.jpg"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers = {'content-type': 'application/json','Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})
        return test_results

    def testInformationValidity(self):
        """ Tests if all information is captured """
        test_party = {
            "id":"1",
            "name":"CCM",
            "hqAddress":"Nairobi Kenya"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers = {'content-type': 'application/json','Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})
        
        self.assertEqual(test_results.status_code, 417)

    def testIDValidity(self):
        """ Tests ID validity """
        test_party = {
            "id":"",
            "name":"CCM",
            "hqAddress":"Nairobi Kenya",
            "logourl":"party.jpg"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers = {'content-type': 'application/json', 'Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})
        
        self.assertEqual(test_results.status_code, 406)

    def testNameValidity(self):
        """ Tests Name Validity """
        test_party = {
            "id":"1",
            "name":"",
            "hqAddress":"Nairobi Kenya",
            "logourl":"party.jpg"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers = {'content-type': 'application/json','Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})
        
        self.assertEqual(test_results.status_code, 406)

    def testAddressValidity(self):
        """ Tests Address Validity """
        test_party = {
            "id":"1",
            "name":"CCM",
            "hqAddress":"",
            "logourl":"party.jpg"
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers = {'content-type': 'application/json','Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})
        
        self.assertEqual(test_results.status_code, 406)

    def testURLValidity(self):
        """ Tests URL Validity """
        test_party = {
            "id":"1",
            "name":"CCM",
            "hqAddress":"Nairobi Kenya",
            "logourl":""
        }

        test_results = self.client.post("api/v1/parties", data=json.dumps(test_party), headers = {'content-type': 'application/json','Authorization': 'Basic {}'.format(base64.b64encode(b'admin:admin').decode('utf8'))})
        
        self.assertEqual(test_results.status_code, 406)

