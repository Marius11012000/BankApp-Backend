# from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo
# from werkzeug.security import generate_password_hash, check_password_hash
#
# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
# mongo = PyMongo(app)
#
# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')
#     cnp = data.get('cnp')
#     phone = data.get('phone')
#     # Validează datele...
#     if username and email and password and cnp and phone:
#         hashed_password = generate_password_hash(password)
#         mongo.db.users.insert_one({
#             'username': username,
#             'email': email,
#             'password': hashed_password,
#             'cnp': cnp,
#             'phone': phone
#         })
#         return jsonify({'message': 'Registered successfully'}), 201
#     else:
#         return jsonify({'message': 'Missing data'}), 400
#
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user = mongo.db.users.find_one({'email': data.get('email')})
#     if user and check_password_hash(user['password'], data.get('password')):
#         return jsonify({'message': 'Login successful'}), 200
#     else:
#         return jsonify({'message': 'Invalid username or password'}), 401


from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

