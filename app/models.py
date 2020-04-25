from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Helper tables for many to many relationships
instructors = db.Table(
    "instructors",
    db.Column("instructor_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("cohort_id", db.Integer, db.ForeignKey("cohort.id"), primary_key=True),
)

students = db.Table(
    "students",
    db.Column("student_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("cohort_id", db.Integer, db.ForeignKey("cohort.id"), primary_key=True),
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean())
    student_in_cohort_id = db.relationship("Cohort", backref="students")

    def __repr__(self):
        return f"<User {self.email}"

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Cohort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    start_date = db.Column(db.Date)
    students = db.relationship("Student", backref="cohort")
    instructors = db.relationship("Instructor", backref="cohort")

    def __repr__(self):
        return f"<Cohort {self.name} starting {self.date}>"


# TODO Implement
# class Cohort_Assignment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


# class Assigment_Template(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


# class User_Assigment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
