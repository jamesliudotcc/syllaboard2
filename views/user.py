from functools import wraps

from flask import Blueprint, request
from flask_json import as_json
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity,
    verify_jwt_in_request,
)

from email_validator import validate_email, EmailNotValidError

from app.models import User, db

user_blueprint = Blueprint("user_blueprint", __name__)


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        current_user = get_jwt_identity()

        if not User.query.filter_by(email=current_user).one().is_admin:
            return {"msg": "Not admin"}, 403
        return fn(*args, **kwargs)

    return wrapper


@user_blueprint.route("/")
@admin_required
@as_json
def user():
    """
    Responds with a list of users
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
