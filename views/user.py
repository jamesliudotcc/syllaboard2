from flask import Blueprint, request
from flask_json import as_json
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity,
)

from email_validator import validate_email, EmailNotValidError

from app.models import User, db

user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/")
@jwt_required
# TODO Instead, use a custom decorator: https://flask-jwt-extended.readthedocs.io/en/stable/custom_decorators/
@as_json
def user():
    """
    Responds with a list of users
    """

    user_fields = {
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_instructor": user.is_instructor,
        "is_admin": user.is_admin,
    }

    # TODO Build a dict based on query params and pass in as **kwargs into filter_by

    return [user_fields for user in User.query.filter_by().all()]
