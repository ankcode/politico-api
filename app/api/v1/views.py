from flask import Blueprint, jsonify, request, Response
from app.api.v1.models import CreateParty, GetAllParties

BASE_URL_BP = Blueprint("V1", __name__, url_prefix='/api/v1')

def login(username, password):
    """ Checks for password and username  """
    return username == 'admin' and password == 'admin'

def check_login():
    return Response(
    'You must be logged in as an admin to create a party.', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_login(creds):

    def getCredentials(*args, **kwargs):

        grant_access = request.authorization

        if not grant_access or not login(grant_access.username, grant_access.password):

            return check_login()

        return creds(*args, **kwargs)

    return getCredentials


@BASE_URL_BP.route('/parties', methods = ['POST'])
@requires_login
def partiesCreate():
    """ Creates a new party if doesnot exist """

    if request.method == 'POST':

        party_val =  request.get_json(force=True)

        msg = CreateParty(party_val)
        return msg

@BASE_URL_BP.route('/parties', methods = ['GET'])
def partiesGetAll():
    """ Fetches all parties """

    if request.method == 'GET':
        msg = GetAllParties()
        
        return msg



