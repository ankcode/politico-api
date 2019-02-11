from flask import Blueprint, jsonify, request, Response, abort, render_template
from jinja2 import TemplateNotFound
from app.api.v1.models import CreateParty, GetAllParties, GetSpecificParty, EditPartyName, DeleteParty, CreateOffice, GetAllOffices, GetSpecificOffice

BASE_URL_BP = Blueprint("V1", __name__, url_prefix='/api/v1')
HOME_PAGE = Blueprint("homepage", __name__, template_folder='templates')


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


@HOME_PAGE.route('/')
def index():
    return render_template('index.html')
    
@BASE_URL_BP.route('/parties', methods=['POST'])
@requires_login
def partiesCreate():
    """ Creates a new party if doesnot exist """

    if request.method == 'POST':

        party_val = request.get_json(force=True)

        msg = CreateParty(party_val)
        return msg


@BASE_URL_BP.route('/parties', methods=['GET'])
def partiesGetAll():
    """ Fetches all parties """

    if request.method == 'GET':
        msg = GetAllParties()

        return msg


@BASE_URL_BP.route('/parties/<party_id>', methods=['GET'])
def partiesGetSpecific(party_id):
    """ Fetches specific party """

    if request.method == 'GET':

        msg = GetSpecificParty(party_id)

        return msg


@BASE_URL_BP.route('/parties/<party_id>/name', methods=['PATCH'])
def EditParty(party_id):
    """ Fetches all parties """

    if request.method == 'PATCH':

        party_name = request.get_json(force=True)

        msg = EditPartyName(party_id, party_name)

        return msg


@BASE_URL_BP.route('/parties/<party_id>', methods=['DELETE'])
def delParty(party_id):
    """ Delete a specific party """

    if request.method == 'DELETE':

        msg = DeleteParty(party_id)

        return msg


@BASE_URL_BP.route('/offices', methods=['POST'])
def officeCreate():
    """ Creates a new office if doesnot exist """

    if request.method == 'POST':

        office_val = request.get_json(force=True)

        msg = CreateOffice(office_val)
        return msg


@BASE_URL_BP.route('/offices', methods=['GET'])
def officesGetAll():
    """ Fetches all offices """

    if request.method == 'GET':
        msg = GetAllOffices()

        return msg

@BASE_URL_BP.route('/offices/<office_id>', methods=['GET'])
def officesGetSpecific(office_id):
    """ Fetches specific office """

    if request.method == 'GET':

        msg = GetSpecificOffice(office_id)

        return msg
