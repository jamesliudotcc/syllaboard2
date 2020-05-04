from flask import Blueprint, request
from flask_json import as_json
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity,
)

from app.models import Cohort, User, db
from views.auth_decorators import admin_required

from app.next_week_start import next_week_start


cohort_blueprint = Blueprint("cohort_blueprint", __name__)


def format_cohort_data(cohort):
    """
    Helper function to retreive the cohort data
    """
    return {
        "id": cohort.id,
        "name": cohort.name,
        "start_date": cohort.start_date,
        "campus": cohort.campus,
        "users": [
            {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
            for user in cohort.users
        ],
    }


@cohort_blueprint.route("/", methods=["GET", "POST"])
@admin_required
@as_json
def cohort():
    """
    get:
        summary: Cohort endpoint
        description:
        responses:
            200:
                description: List of the most recent 10 cohorts.
    post:
        summary: Create a cohort
        description: '''
        resp = await fetch('http://localhost:5000/cohort/', 
          {method: 'POST',
          headers: {'Content-Type': 'application/json', Authorization: `Bearer ${body.access_token}`},
          body: JSON.stringify({users: [4, 5, 6], name: "UXDI 2"})}
        )

        '''
        responses:
            201:
                description: 


    """
    if request.method == "GET":
        cohorts = [format_cohort_data(cohort) for cohort in Cohort.query.all()]
        return {"data": cohorts}

    if request.method == "POST":
        name = request.json.get("name")
        start_date = request.json.get("start_date", None)
        campus = request.json.get("campus", None)
        users = request.json.get("users", None)

        if not name:
            return {"error": "No Cohort name"}, 422

        if not start_date:
            start_date = next_week_start()

        if not campus:
            campus = "Remote LA"

        cohort = Cohort(name=name, start_date=start_date, campus=campus)
        for user in users:
            cohort.users.append(User.query.get(user))
        db.session.add(cohort)
        db.session.commit()

        cohort = Cohort.query.filter_by(**{"name": name, "campus": campus}).first()
        return {"data": format_cohort_data(cohort)}


@cohort_blueprint.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
@admin_required
@as_json
def cohort_each(id):
    """
    get:
        summary: Individual cohort endpoint
        description: 
        responses:
            200:
                description: The requested 
    put:
        summary: Edit a cohort
        description: {users: userId[]}
        responses:
            200:
                description:
                '''
                resp = await fetch('http://localhost:5000/cohort/1', {
                  method: 'PUT', 
                  headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${body.access_token}`
                  },
                  body: JSON.stringify({users: [1, 2, 3]})
                })
                '''


    """

    cohort = Cohort.query.get(id)
    if cohort is None:
        return {"error": "not found"}, 404

    if request.method == "GET":
        return {"data": format_cohort_data(cohort)}

    if request.method == "PUT":
        users = request.json.get("users", None)
        for user in users:
            cohort.users.append(User.query.get(user))
        db.session.add(cohort)
        db.session.commit()

        cohort = Cohort.query.get(id)

        return {"data": format_cohort_data(cohort)}

    if request.method == "DELETE":
        db.session.delete(cohort)
        db.session.commit()
        return {"data": {"deleted": id}}
