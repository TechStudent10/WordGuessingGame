from flask_sqlalchemy import SQLAlchemy
import random, string

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    is_host = db.Column(db.Boolean, default=False)
    game_id = db.Column(db.ForeignKey('game.id'))
    score = db.Column(db.Integer, default=0)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String(6), default=''.join(random.choices(
        string.ascii_letters,
        k=6
    )))
    users = db.relationship('User', backref='game')
    current_word = db.Column(db.String(100), nullable=True)