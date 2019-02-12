from datetime import datetime
from flask import jsonify

""" Dictionary containing parties """

political_parties = {}

class PoliticalParties:

    @staticmethod
    def create_party(party_data):
        msgResponse = ''

        if len(party_data) < 3:

            """ check if submitted data is complete, i.e has all parameters required"""

            responseCreated = {"status": 406,
                            "message": "The information provided is incomplete please update to proceed"
                            }

            msgResponse = jsonify(responseCreated), 406

        elif any(political_parties[i]["name"] == party_data["name"] for i in political_parties.keys()) and (party_data["hqAddress"].strip() != "" and party_data["logourl"].strip() != ""):

            """ check if party has already been created and return already created message if true """

            responseCreated = {"status": 400,
                            "message": "The party already exists"
                            }

            msgResponse = jsonify(responseCreated), 400

        elif str(party_data["name"]) == "":

            """ check if party name enetered is valid """

            responseCreated = {"status": 406,
                            "message": "Please enter a valid name!"
                            }

            msgResponse = jsonify(responseCreated), 406

        elif str(party_data["hqAddress"]) == "":

            """ check if party address enetered is valid """

            responseCreated = {"status": 406,
                            "message": "Please enter a valid Address!"
                            }

            msgResponse = jsonify(responseCreated), 406

        elif str(party_data["logourl"]) == "":

            """ check if party logourl enetered is valid """

            responseCreated = {"status": 406,
                            "message": "Please enter a valid url!"
                            }

            msgResponse = jsonify(responseCreated), 406

        else:

            """ Add party to list if all conditions are met """

            id_count = len(political_parties)
            id_count = id_count + 1

            party_data["datecreated"] = datetime.utcnow()
            party_data['id'] = id_count

            political_parties[id_count] = party_data

            responseCreated = {"status": 201,
                            "data": party_data
                            }
            msgResponse = jsonify(responseCreated), 201

        return msgResponse


    @staticmethod
    def get_all_parties():
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

    @staticmethod
    def get_specific_party(partyid):
        msgResponse = ""

        if len(political_parties) != 0:

            if partyid in political_parties:

                party_data = political_parties[partyid]

                responseCreated = {"status": 200,
                                "data": [party_data]
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


    @staticmethod
    def edit_party_name(party_id, party_name):
        """ Edits name of a specific party """

        msgResponse = ""

        if len(political_parties) != 0:

            if party_id in political_parties:

                political_parties[party_id]["id"] = party_id
                political_parties[party_id]["name"] = party_name["name"]

                party_data = dict(id=party_id, name=party_name["name"])

                responseCreated = {"status": 200,
                                "data": [party_data]
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


    @staticmethod
    def delete_party(partyid):
        """ Deletes specific party  """
        msgResponse = ""

        if len(political_parties) != 0:

            if partyid in political_parties:

                del political_parties[partyid]

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