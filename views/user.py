from flask import Blueprint, request
from flask_json import as_json
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity,
)

from email_validator import validate_email, EmailNotValidError

from app.models import User, db
from views.auth_decorators import admin_required

user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/")
@admin_required
@as_json
def user():
    """
    Responds with a list of users
    TODO query string based on unassigned
    TODO query string based on instructor or not
    TODO query string based on admin or not
    """

    # TODO Build a dict based on query params and pass in as **kwargs into filter_by

    return [
        {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_instructor": user.is_instructor,
            "is_admin": user.is_admin,
        }
        for user in User.query.filter_by().all()
    ]
