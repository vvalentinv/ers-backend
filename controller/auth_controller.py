from flask import Blueprint, request, jsonify
from exception.Unauthorized import Unauthorized
from service.auth_service import AuthService
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
import flask

ac = Blueprint('auth_controller', __name__)
auth_service = AuthService()


@ac.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == "OPTIONS":
        resp = flask.Response("preflight")
        # resp.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
        resp.headers["Access-Control-Allow-Origin"] = "https://ers-frontend.herokuapp.com"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Content-Length, Accept"
        resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        return resp

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    try:
        # Access - Control - Allow - Origin: *

        user = auth_service.login(username, password)
        print(user)
        resp = flask.Response("login")
        resp.access_control_allow_origin = "https://ers-frontend.herokuapp.com"
        # resp.access_control_allow_origin = "http://127.0.0.1:5500"
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        resp.response = jsonify("msg", "Login successfully")
        access_token = create_access_token(identity={"user_id": user.get_user_id(),
                                                     "username": user.get_username(),
                                                     "first_name": user.get_first_name(),
                                                     "last_name": user.get_last_name(),
                                                     "email": user.get_email(),
                                                     "user_role": user.get_user_role()})
        set_access_cookies(resp.response, access_token)

        return resp
    except Unauthorized as e:
        return {
                   "message": str(e)
               }, 401


@ac.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response, 200
