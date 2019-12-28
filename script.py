from flask import Flask, request

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

@app.route('/sendit/api/v1/signup', methods = ['POST'])
def createUser():
    user = {
        "user_id" : users[-1]['user_id'] + 1,
        "full_name" : request.json['full_name'],
        "user_name" : request.json['user_name'],
        "email" : request.json["email"],
        "password" : request.json["password"]
    }
    users.append(user)
    return jsonify({"user":user}), 201




if __name__ == '__main__':
    app.run(debug = True)
