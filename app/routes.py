# /app/routes.py

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import mongo

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)  # force=True ajută la preluarea datelor JSON chiar dacă content-type header nu este setat corect
    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    address = data.get('address')
    cnp = data.get('cnp')
    phone = data.get('phone')
    image_base64 = data.get('image')  # Imaginea profilului
    self_image_base64 = data.get('self_image')  # Imaginea selfie
    validation_after_verification = 0 # se face 1 dupa ce administratorul
                                      # verifica datele introduse si fotografiile

    if not all([username, firstname, lastname, email, password, confirm_password, address, cnp, phone, image_base64, self_image_base64]):
        return jsonify({'message': 'Lipsesc date necesare pentru inregistrare.'}), 400

    if mongo.db.users.find_one({'email': email}):
        return jsonify({'message': 'Exista deja un utilizator cu acest email.'}), 409

    if mongo.db.users.find_one({'cnp': cnp}):
        return jsonify({'message': 'Exista deja un utilizator cu acest cnp.'}), 409

    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({
        'username': username,
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'password': hashed_password,
        'address': address,
        'cnp': cnp,
        'phone': phone,
        'image': image_base64,  # Salvare imagine profil
        'self_image': self_image_base64,  # Salvare imagine selfie
        'validation': validation_after_verification
    })
    return jsonify({'message': 'Utilizator inregistrat cu succes.'}), 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = mongo.db.users.find_one({'email': data['email']})

    if user and check_password_hash(user['password'], data['password']):
        user_data = {
            "email": user["email"],
            "username": user.get("username", ""),
            "firstname": user.get("firstname", ""),
            "lastname": user.get("lastname", ""),
            "phone": user.get("phone", ""),
            "cnp": user.get("cnp", ""),
            'address': user.get("address", "")
        }

        if "_id" in user:
            user_data["_id"] = str(user["_id"])

        return jsonify({'message': 'Autentificare reusita', 'user': user_data}), 200
    else:
        return jsonify({'error': 'Email sau parola gresita'}), 401