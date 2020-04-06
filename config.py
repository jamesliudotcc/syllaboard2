from dotenv import load_dotenv
import os


load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Howto: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
    """

    JWT_SECRET_KEY = JWT_SECRET_KEY or "itshopeless"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
