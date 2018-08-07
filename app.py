# -*- coding: utf-8 -*-


from flask import Flask, jsonify, request, render_template, json
from database import Database
from helpers import convert_date
from flask_cors import CORS


# Configuration
DEBUG = True


# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)
db = Database()


# Functios to call Database
def db_query():
    db = Database()
    users = db.user_list()
    return users


def db_user(user_id):
    db = Database()
    user = db.get_user(user_id)
    return user


# Get Users
@app.route('/users', methods=['GET'])
def users():
    users = db_query()
    user_object = []

    if request.method == 'GET':
        for user in users:
            if user['updated_date'] == None:
                updated_date = None
            else:
                updated_date = convert_date(user['updated_date'])
            user_object.append({
                'id': user['id'],
                'user_name': user['user_name'],
                'status': user['status'],
                'prev_status': user['prev_status'],
                'created_date': convert_date(user['created_date']),
                'updated_date': updated_date
            })
    else:
        return jsonify(user_object)
    return jsonify({'users': user_object})


# Add Users
@app.route('/add', methods=['POST'])
def add_users():
    response_object = {}

    if request.method == 'POST':
        post_data = request.get_json()
        user_name = post_data.get('user_name')
        status = post_data.get('status')
        user = db.add_user(user_name, status)
        print(user)
        response_object['message'] = 'User added!'
        # return jsonify(response_object)
    else:
        return "Something went wrong!"
    return jsonify(response_object)


# Get User
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = db.get_user(user_id)
    data_object = {'message': 'No user found!'}

    if request.method == 'GET':
        for u in user:
            if u['updated_date'] != None:
                updated_date = convert_date(u['updated_date'])
            else:
                updated_date = u['updated_date']
            data_object = {
                'id': u['id'],
                'user_name': u['user_name'],
                'status': u['status'],
                'prev_status': u['prev_status'],
                'created_date': convert_date(u['created_date']),
                'updated_date': updated_date
            }
            # return jsonify(data_object)
        return jsonify(data_object)
    else:
        return "Something went wrong!"


# Edit User
@app.route('/user/<user_id>/edit', methods=['PUT'])
def edit_user(user_id):
    response_object = {}
    user = db.get_user(user_id)
    for u in user:
        recent_status = ''
        recent_status = u['prev_status']
        if recent_status == "":
            recent_status = u['status']
        elif recent_status == u['prev_status']:
            recent_status = u['status']
        else:
            recent_status = u['prev_status']

    if request.method == 'PUT':
        post_data = request.get_json()
        user_name = post_data.get('user_name'),
        status = post_data.get('status'),
        prev_status = recent_status
        print(prev_status)
        user = db.edit_user(user_name, status, prev_status, user_id)

        response_object['message'] = 'User successfully edited!'
        # return jsonify(response_object)
    else:
        return "Something went wrong!"
    return jsonify(response_object)


# Delete User
@app.route('/user/<user_id>/delete', methods=['POST'])
def delete_user(user_id):
    response_object = {'message': 'No user found!'}

    if request.method == 'POST':
        user = db.delete_user(user_id)
        print(user)
        response_object['message'] = 'User successfully deleted!'
        # return jsonify(response_object)
    else:
        return "Something went wrong!"
    return jsonify(response_object)


# Restore User
@app.route('/user/<user_id>/restore', methods=['POST'])
def restore_user(user_id):
    response_object = {'message': 'No user found!'}

    if request.method == 'POST':
        user = db.restore_user(user_id)
        print(user)
        response_object['message'] = 'User successfully restored!'
        # return jsonify(response_object)
    else:
        return "Something went wrong!"
    return jsonify(response_object)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def special_exception_handler(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host="localhost", port=5000, threaded=True, debug=True)
