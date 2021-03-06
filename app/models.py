from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from app.next_week_start import next_week_start

db = SQLAlchemy()

# Helper tables for many to many relationships

user_cohort = db.Table(
    "user_cohort",
    db.Column("student_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("cohort_id", db.Integer, db.ForeignKey("cohort.id"), primary_key=True),
)


@dataclass
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False)
    # TODO Instructor should have a campus attached
    is_instructor = db.Column(db.Boolean(), nullable=False)
    user_cohort = db.relationship("Cohort", secondary=user_cohort, backref="users")
    user_assignment_templates = db.relationship(
        "Assignment_Template", backref="user", lazy=True
    )
    user_assignments = db.relationship("User_Assignment", backref="user", lazy=False)

    def __repr__(self):
        return f"<User {self.email}, Instructor: {self.is_instructor} Admin: {self.is_admin}>"

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


@dataclass
class Cohort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    campus = db.Column(db.String, nullable=False, server_default="Remote LA")
    cohort_assignments = db.relationship(
        "Cohort_Assignment", lazy=False, backref="cohort"
    )
    # Time zone is an application concern, not DB

    def __repr__(self):
        return f"<Cohort {self.name} starting {self.start_date}>"


class Assignment_Template(db.Model):
    __tablename__ = "assignment_template"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    detail = db.Column(db.UnicodeText, nullable=False)
    version = db.Column(db.Integer, nullable=False, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    cohort_assignments = db.relationship(
        "Cohort_Assignment",
        lazy=True,
        backref=db.backref("assignment_template", lazy=True),
    )


# TODO Implement
class Cohort_Assignment(db.Model):
    __tablename__ = "cohort_assignment"

    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Date, nullable=False)
    due = db.Column(db.Date, nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey("assignment_template.id"))
    cohort_id = db.Column(db.Integer, db.ForeignKey("cohort.id"))
    cohort_assignment_user_assignments = db.relationship(
        "User_Assignment", backref="cohort_assignment", lazy=True
    )


class User_Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128), nullable=False)
    grade = db.Column(db.Integer, nullable=True)
    student_comment = db.Column(db.UnicodeText, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    cohort_assignmet_id = db.Column(db.Integer, db.ForeignKey("cohort_assignment.id"))
