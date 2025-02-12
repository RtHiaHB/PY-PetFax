from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('pets/index.html', pets = pets)

@bp.route('/<pet_id>')
def individual_pets(pet_id):
    pet = {}
    for eachpet in pets:
        if eachpet['pet_id'] == int(pet_id):
            pet = eachpet
    return render_template('pets/pet.html', pet = pet)