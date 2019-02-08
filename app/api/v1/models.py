from datetime import datetime
from flask import jsonify

""" List containing parties """
political_parties=[]

def CreateParty(data_party):
    msgResponse = ''

    if len(data_party) < 4:

        """ check if submitted data is complete, i.e has all parameters required"""

        msgResponse = "The information provided is incomplete please update to proceed", 417


    elif any(data_res['name'].strip() == data_party['name'].strip() for data_res in political_parties) and (data_party['name'].strip() != "" and  data_party['id'].strip() != "" and data_party['hqAddress'].strip() != "" and  data_party['logourl'].strip() != ""):
 
        
        """ check if party has already been created and return already created message if true """

        msgResponse = "Party already exists", 400

    elif not data_party["id"].isdigit():

        """ check if party id enetered is valid """

        msgResponse = "Your ID should be an integer!", 406

    elif str(data_party["name"]) == "":

        """ check if party name enetered is valid """

        msgResponse = "Please enter a valid name!", 406

    elif str(data_party["hqAddress"]) == "":

        """ check if party address enetered is valid """

        msgResponse = "Please enter a valid Address!", 406
    
    elif str(data_party["logourl"]) == "" :

        """ check if party logourl enetered is valid """

        msgResponse = "Please enter a valid url!", 406

    else:

        """ Add party to list if all conditions are met """
        data_party["datecreated"] = datetime.utcnow()

        political_parties.append(data_party)
        msgResponse = jsonify(data_party), 201

    return msgResponse


def GetAllParties():

    """ Fetch all political parties """
    
    msgResponse = ''
    if len(political_parties) > 0:

        msgResponse = jsonify(political_parties), 200

    else:
        msgResponse = "No party created", 200

    return msgResponse

def GetSpecificParty(partyid):
    msgResponse = ""

    if len(political_parties) != 0:

        for party in political_parties:
            if party['id'] == partyid and party['id'] != "":

                data_party = party
                msgResponse = jsonify(data_party), 200

            else:

                msgResponse = "Party Not found", 404
            
    else:

         msgResponse = "No parties found", 404
        
    return msgResponse


def EditPartyName(party_id, party_name):
    """ Edits name of a specific party """

    msgResponse = ""

    if len(political_parties) != 0:

        for party in political_parties:
            if party['id'] == party_id:

                party['name'] = party_name['name']

                data_party = dict(id=party_id, name=party['name'])

                msgResponse = jsonify(data_party), 200

            else:

                msgResponse = "Party Not found", 404
            
    else:

         msgResponse = "No parties found", 404
        
    return msgResponse


def DeleteParty(partyid):
    """ Deletes specific party  """
    msgResponse = ""

    if len(political_parties) != 0:

        for party in political_parties:
            if party['id'] == partyid and party['id'] != "":

                political_parties.remove(party)
                msgResponse = jsonify(political_parties), 200

            else:

                msgResponse = "Party Not found", 404
            
    else:

         msgResponse = "No parties found", 404
        
    return msgResponse


    


    

