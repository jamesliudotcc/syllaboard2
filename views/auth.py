from flask import Blueprint, request
from flask_json import as_json
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity,
)

from email_validator import validate_email, EmailNotValidError

from app.models import User, db


auth_blueprint = Blueprint("auth_blueprint", __name__)


@auth_blueprint.route("/me")
@jwt_required
@as_json
def me():
    """
    Responds with username. Used to test that login is current
    """
    current_user = get_jwt_identity()
    return {"logged_in_as": current_user}, 200


@auth_blueprint.route("/login", methods=["POST"])
@as_json
def login():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    try:
        v = validate_email(email)
        email = v["email"]  # replace with normalized form
    except EmailNotValidError as e:
        return {"msg": str(e)}, 422

    if not email or not password:
        return {"msg": "Bady formed JSON request"}, 400

    user = User.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        return {"msg": "Bad email or password"}, 401

    access_token = create_access_token(identity=email)
    return {"access_token": access_token}, 200


@auth_blueprint.route("/register", methods=["POST"])
@as_json
def register():
    if not request.is_json:
        return {"msg": "Missing JSON in request"}, 400

    email = request.json.get("email", None)
    password = request.json.get("password", None)
    first_name = request.json.get("first_name", None)
    last_name = request.json.get("last_name", None)

    if not email or not password:
        return {"msg": "Bady formed JSON request"}, 400

    try:
        v = validate_email(email)
        email = v["email"]  # replace with normalized form
    except EmailNotValidError as e:
        return {"msg": str(e)}, 422

    if User.query.filter_by(email=email).first():
        return {"msg": "User already exists with that email"}, 422

    user = User(email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)

    if User.query.filter_by(is_admin=True).count() == 0:
        user.is_admin = True

    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=email)
    return {"access_token": access_token}, 200
