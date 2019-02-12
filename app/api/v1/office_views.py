from flask import Blueprint, jsonify, request
from app.api.v1.office_models import PoliticalOffices

BASE_URL_BP = Blueprint("offices", __name__, url_prefix='/api/v1')

@BASE_URL_BP.route('/offices', methods=['POST'])
def createOffice():
    """ Creates a new party if doesnot exist """

    if request.method == 'POST':

        office_val = request.get_json(force=True)

        msg = PoliticalOffices.create_office(office_val)
    return msg

@BASE_URL_BP.route('/offices', methods=['GET'])
def partiesGetAll():
    """ Fetches all parties """

    if request.method == 'GET':
        msg = PoliticalOffices.get_all_offices()

    return msg

@BASE_URL_BP.route('/offices/<int:office_id>', methods=['GET'])
def partiesGetSpecific(office_id):
    """ Fetches specific party """

    if request.method == 'GET':

        msg = PoliticalOffices.get_specific_office(office_id)

    return msg
