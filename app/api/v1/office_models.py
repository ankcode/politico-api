from datetime import datetime
from flask import jsonify

""" Dictionary containing offices """

political_offices = {}


class PoliticalOffices:

    @staticmethod
    def create_office(data_office):
        msgResponse = ''

        if len(data_office) < 2:

            """ check if submitted data is complete, i.e has all parameters required"""

            msgResponse = "The information provided is incomplete please update to proceed", 406

        elif any(political_offices[i]['name'] == data_office['name'].strip() for i in political_offices.keys()) and (data_office['name'].strip() != "" and data_office['type'].strip() != ""):

            """ check if office has already been created and return already created message if true """

            responseCreated = {"status": 400,
                               "data": "office already exists"
                               }

            msgResponse = jsonify(responseCreated), 400

        elif str(data_office["name"]) == "":

            """ check if office name enetered is valid """

            responseCreated = {"status": 406,
                               "message": "Please enter a valid name!"
                               }

            msgResponse = jsonify(responseCreated), 406

        elif str(data_office["type"]) == "":

            """ check if office type enetered is valid """

            responseCreated = {"status": 406,
                               "message": "Please enter a valid office type!"
                               }

            msgResponse = jsonify(responseCreated), 406

        else:

            """ Add office to list if all conditions are met """

            id_count = len(political_offices)
            id_count = id_count + 1

            data_office["datecreated"] = datetime.utcnow()
            data_office['id'] = id_count

            political_offices[id_count] = data_office

            responseCreated = {"status": 201,
                               "data": [data_office]
                               }
            msgResponse = jsonify(responseCreated), 201

        return msgResponse

    @staticmethod
    def get_all_offices():
        """ Fetch all political offices """

        msgResponse = ''
        if len(political_offices) > 0:

            responseCreated = {"status": 200,
                               "data": political_offices
                               }
            msgResponse = jsonify(responseCreated), 200

        else:

            responseCreated = {"status": 200,
                               "message": "No offices created yet."
                               }

            msgResponse = jsonify(responseCreated), 200

        return msgResponse

    @staticmethod
    def get_specific_office(officeid):

        msgResponse = ""

        if len(political_offices) != 0:

            if officeid in political_offices:

                office_data = political_offices[officeid]

                responseCreated = {"status": 200,
                                   "data": office_data
                                   }
                msgResponse = jsonify(responseCreated), 200

            else:

                responseCreated = {"status": 404,
                                   "message": "Party not found."
                                   }

                msgResponse = jsonify(responseCreated), 404

        else:

            responseCreated = {"status": 404,
                               "message": "No parties found"
                               }

            msgResponse = jsonify(responseCreated), 404

        return msgResponse
