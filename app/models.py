from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Helper tables for many to many relationships

user_cohort = db.Table(
    "user_cohort",
    db.Column("student_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("cohort_id", db.Integer, db.ForeignKey("cohort.id"), primary_key=True),
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False)
    is_instructor = db.Column(db.Boolean(), nullable=False)
    user_cohort = db.relationship("Cohort", secondary=user_cohort, backref="cohort")

    def __repr__(self):
        return f"<User {self.email}, Instructor: {self.is_instructor} Admin: {self.is_admin}>"

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Cohort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    start_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Cohort {self.name} starting {self.date}>"


# TODO Implement
# class Cohort_Assignment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


# class Assigment_Template(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


# class User_Assigment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
