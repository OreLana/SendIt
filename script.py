from flask import Flask, request, jsonify, abort
import re

app = Flask(__name__)


users = [
    {
        "user_id" : 0,
        "full_name" : "Lana Oreoluwa",
        "user_name": "OreLana",
        "email" : "lana@yahoo.com",
        "password" : "sharon12"
    },
    {
        "user_id" : 1,
        "full_name" : "Lana Ifeoluwa",
        "user_name": "IfeLana",
        "email" : "lana@yahoo.com",
        "password" : "sharon12"
    },
    {
        "user_id" : 2,
        "full_name" : "Lana Daniella",
        "user_name": "DanLana",
        "email" : "lana@yahoo.com",
        "password" : "sharon12"
    }
]

parcels = [
    {
        "parcel_id": 1,
        "current_location" : "Nigeria",
        "destination" : "Uinted Kingdom",
        "no_of_parcels" : 1,
        "weight" : 23,
        "lenght" : 14,
        "height" : 12,
        "width" : 10
    },
    {
        "parcel_id": 1,
        "current_location" : "Nigeria",
        "destination" : "Uinted Ireland",
        "no_of_parcels" : 1,
        "weight" : 40,
        "lenght" : 12,
        "height" : 13,
        "width" : 10
    }
]

@app.route('/sendit/api/v1/signup', methods = ['POST'])
def createUser():
    post_data = request.get_json()
    user = {
        "user_id" : users[-1]['user_id'] + 1,
        "full_name" : post_data.get("fullname"),
        "user_name" : post_data.get('username'),
        "email" : post_data.get("email"),
        "password" : post_data.get("password")
    }
    if user['full_name'] == "" or user['password'] == "":
        abort(400) 
    if ((user["full_name"]).replace(" ","")).isalpha() == False:
        abort(400)
    else:    
        users.append(user)
        return jsonify(users)



'''@app.route('/sendit/api/v1/parcel', methods = ['POST'])
def createParcel():
    user = {
        "parecl_id" : users[-1]['parcel_id'] + 1,
        "full_name" : request.json['full_name'],
        "user_name" : request.json['user_name'],
        "email" : request.json["email"],
        "password" : request.json["password"]
    }
    users.append(user)
    return jsonify({"user":user}), 201
'''


if __name__ == '__main__':
    app.run(debug = True)
