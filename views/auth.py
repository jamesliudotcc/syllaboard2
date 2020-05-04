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
    get:
        summary: Responds with username. Used to test that login is current
    """
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).one()
    return (
        {
            "data": {
                "logged_in_as": current_user,
                "admin": user.is_admin,
                "instructor": user.is_instructor,
            }
        },
        200,
    )


@auth_blueprint.route("/login", methods=["POST"])
@as_json
def login():
    if not request.is_json:
        return {"error": "Missing JSON in request"}, 400

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    try:
        v = validate_email(email)
        email = v["email"]  # replace with normalized form
    except EmailNotValidError as e:
        return {"error": str(e)}, 422

    if not email or not password:
        return {"error": "Bady formed JSON request"}, 400

    user = User.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        return {"error": "Bad email or password"}, 401

    access_token = create_access_token(identity=email)
    return {"access_token": access_token}, 200


@auth_blueprint.route("/register", methods=["POST"])
@as_json
def register():
    if not request.is_json:
        return {"error": "Missing JSON in request"}, 400

    email = request.json.get("email", None)
    password = request.json.get("password", None)

    try:
        v = validate_email(email)
        email = v["email"]  # replace with normalized form
    except EmailNotValidError as e:
        return {"error": str(e)}, 422

    new_user = {
        "email": email,
        "first_name": request.json.get("first_name", None),
        "last_name": request.json.get("last_name", None),
        "is_instructor": False,
        "is_admin": False,
    }

    if User.query.filter_by(email=email).first():
        return {"error": "User already exists with that email"}, 422

    if User.query.filter_by(is_admin=True).count() == 0:
        new_user["is_admin"] = True

    user = User(**new_user)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=email)
    return {"access_token": access_token}, 200
