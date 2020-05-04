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
    resp = await fetch(`http://localhost:5000/user/?${qs.stringify({lacks_cohort: true})}`, {headers: { Authorization: `Bearer ${body.access_token}` } })
    """
    filter_conditions = {}

    if request.args.get("lacks_cohort"):
        filter_conditions["user_cohort"] = None

    for condition in ["is_admin", "is_instructor"]:
        if request.args.get(condition):
            filter_conditions[condition] = True

    return {
        "data": [
            {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "is_instructor": user.is_instructor,
                "is_admin": user.is_admin,
            }
            for user in User.query.filter_by(**filter_conditions).all()
        ]
    }
