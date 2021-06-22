from flask import Flask
from dotenv import load_dotenv

import os
if '.env' in os.listdir():
    load_dotenv('.env')

def create_app(*args, **kwargs):
    app = Flask(
        __name__,
        *args,
        **kwargs
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .routes import routes
    app.register_blueprint(routes)

    from .models import db
    db.init_app(app)

    if os.environ.get('DATABASE_URL') is not None:
        db.create_all(app=app)

    return app