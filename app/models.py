from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.email}"

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)