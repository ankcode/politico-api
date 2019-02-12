from flask import Blueprint, jsonify, request, Response, abort, render_template
from jinja2 import TemplateNotFound
from app.api.v1.party_models import PoliticalParties

BASE_URL_BP = Blueprint("parties", __name__, url_prefix='/api/v1')
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

        msg = PoliticalParties.create_party(party_val)
        return msg


@BASE_URL_BP.route('/parties', methods=['GET'])
def partiesGetAll():
    """ Fetches all parties """

    if request.method == 'GET':
        msg = PoliticalParties.get_all_parties()

        return msg


@BASE_URL_BP.route('/parties/<int:party_id>', methods=['GET'])
def partiesGetSpecific(party_id):
    """ Fetches specific party """

    if request.method == 'GET':

        msg = PoliticalParties.get_specific_party(party_id)

        return msg


@BASE_URL_BP.route('/parties/<int:party_id>/name', methods=['PUT'])
def EditParty(party_id):
    """ Fetches all parties """

    if request.method == 'PUT':

        party_name = request.get_json(force=True)

        msg = PoliticalParties.edit_party_name(party_id, party_name)

        return msg


@BASE_URL_BP.route('/parties/<int:party_id>', methods=['DELETE'])
def delParty(party_id):
    """ Delete a specific party """

    if request.method == 'DELETE':

        msg = PoliticalParties.delete_party(party_id)

        return msg