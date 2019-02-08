from datetime import datetime
from flask import jsonify

""" List containing parties """
political_parties = []
political_office = []


def CreateParty(data_party):
    msgResponse = ''

    if len(data_party) < 4:

        """ check if submitted data is complete, i.e has all parameters required"""

        responseCreated = {"status": 406,
                           "message": "The information provided is incomplete please update to proceed"
                           }

        msgResponse = jsonify(responseCreated), 406

    elif any(data_res['name'].strip() == data_party['name'].strip() for data_res in political_parties) and (data_party['name'].strip() != "" and data_party['id'].strip() != "" and data_party['hqAddress'].strip() != "" and data_party['logourl'].strip() != ""):

        """ check if party has already been created and return already created message if true """

        responseCreated = {"status": 400,
                           "message": "The party already exists"
                           }

        msgResponse = jsonify(responseCreated), 400

    elif not data_party["id"].isdigit():

        """ check if party id enetered is valid """

        responseCreated = {"status": 406,
                           "message": "Your ID should be an integer!"
                           }

        msgResponse = jsonify(responseCreated), 406

    elif str(data_party["name"]) == "":

        """ check if party name enetered is valid """

        responseCreated = {"status": 406,
                           "message": "Please enter a valid name!"
                           }

        msgResponse = jsonify(responseCreated), 406

    elif str(data_party["hqAddress"]) == "":

        """ check if party address enetered is valid """

        responseCreated = {"status": 406,
                           "message": "Please enter a valid Address!"
                           }

        msgResponse = jsonify(responseCreated), 406

    elif str(data_party["logourl"]) == "":

        """ check if party logourl enetered is valid """

        responseCreated = {"status": 406,
                           "message": "Please enter a valid url!"
                           }

        msgResponse = jsonify(responseCreated), 406

    else:

        """ Add party to list if all conditions are met """
        data_party["datecreated"] = datetime.utcnow()

        political_parties.append(data_party)
        responseCreated = {"status": 201,
                           "data": [data_party]
                           }
        msgResponse = jsonify(responseCreated), 201

    return msgResponse


def GetAllParties():
    """ Fetch all political parties """

    msgResponse = ''
    if len(political_parties) > 0:

        responseCreated = {"status": 200,
                           "data": political_parties
                           }
        msgResponse = jsonify(responseCreated), 200

    else:

        responseCreated = {"status": 200,
                           "message": "No party created"
                           }

        msgResponse = jsonify(responseCreated), 200

    return msgResponse


def GetSpecificParty(partyid):
    msgResponse = ""

    if len(political_parties) != 0:

        for party in political_parties:
            if party['id'] == partyid and party['id'] != "":

                data_party = party

                responseCreated = {"status": 200,
                                   "data": [data_party]
                                   }
                msgResponse = jsonify(responseCreated), 200

            else:

                responseCreated = {"status": 404,
                                   "message": "Party not found"
                                   }

                msgResponse = jsonify(responseCreated), 404

    else:

        responseCreated = {"status": 404,
                           "message": "No parties found"
                           }

        msgResponse = jsonify(responseCreated), 404

    return msgResponse


def EditPartyName(party_id, party_name):
    """ Edits name of a specific party """

    msgResponse = ""

    if len(political_parties) != 0:

        for party in political_parties:
            if party['id'] == party_id:

                party['name'] = party_name['name']

                data_party = dict(id=party_id, name=party['name'])

                responseCreated = {"status": 200,
                                   "data": [data_party]
                                   }
                msgResponse = jsonify(responseCreated), 200

            else:

                responseCreated = {"status": 404,
                                   "message": "Party not found"
                                   }

                msgResponse = jsonify(responseCreated), 404

    else:

        responseCreated = {"status": 404,
                           "message": "No parties found"
                           }

        msgResponse = jsonify(responseCreated), 404

    return msgResponse


def DeleteParty(partyid):
    """ Deletes specific party  """
    msgResponse = ""

    if len(political_parties) != 0:

        for party in political_parties:
            if party['id'] == partyid and party['id'] != "":

                political_parties.remove(party)

                responseCreated = {"status": 200,
                                   "data": political_parties
                                   }
                msgResponse = jsonify(responseCreated), 200

            else:

                responseCreated = {"status": 404,
                                   "message": "Party not found"
                                   }

                msgResponse = jsonify(responseCreated), 404

    else:

        responseCreated = {"status": 404,
                           "message": "No parties found"
                           }

        msgResponse = jsonify(responseCreated), 404

    return msgResponse


def CreateOffice(data_office):
    msgResponse = ''

    if len(data_office) < 3:

        """ check if submitted data is complete, i.e has all parameters required"""

        msgResponse = "The information provided is incomplete please update to proceed", 406

    elif any(data_office_res['name'].strip() == data_office['name'].strip() for data_office_res in political_office) and (data_office['name'].strip() != "" and data_office['id'].strip() != "" and data_office['type'].strip() != ""):

        """ check if office has already been created and return already created message if true """

        responseCreated = {"status": 400,
                           "data": "office already exists"
                           }

        msgResponse = jsonify(responseCreated), 400

    elif not data_office["id"].isdigit():

        """ check if office id enetered is valid """

        responseCreated = {"status": 406,
                           "message": "Your ID should be an integer!"
                           }

        msgResponse = jsonify(responseCreated), 406

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
        data_office["datecreated"] = datetime.utcnow()

        political_office.append(data_office)
        responseCreated = {"status": 201,
                           "data": [data_office]
                           }
        msgResponse = jsonify(responseCreated), 201

    return msgResponse


def GetAllOffices():
    """ Fetch all political offices """

    msgResponse = ''
    if len(political_office) > 0:

        responseCreated = {"status": 200,
                           "data": political_office
                           }
        msgResponse = jsonify(responseCreated), 200

    else:

        responseCreated = {"status": 200,
                           "message": "No offices created yet."
                           }

        msgResponse = jsonify(responseCreated), 200

    return msgResponse
