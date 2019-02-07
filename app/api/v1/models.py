from datetime import datetime
from flask import jsonify

""" List containing parties """
political_parties=[]

def CreateParty(data_party):
    msgResponse = ''

    if data_party in political_parties: 
        
        """ check if party has already been created and return already created message if true """

        msgResponse = "Party already exists", 400

    elif len(data_party) < 4:

        """ check if submitted data is complete, i.e has all parameters required"""

        msgResponse = "The information provided is incomplete please update to proceed", 417

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

    


    

