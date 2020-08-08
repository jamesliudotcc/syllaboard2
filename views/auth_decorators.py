from functools import wraps
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity,
    verify_jwt_in_request,
)

from app.models import User, db


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        current_user = get_jwt_identity()

        if not User.query.filter_by(email=current_user).one().is_admin:
            return {"error": "Not admin"}, 403
        return fn(*args, **kwargs)

    return wrapper


# TODO Create instructor required.
