from flask import Blueprint, render_template, redirect, url_for, abort
from .models import db, User, Game

routes = Blueprint(
    'routes',
    __name__
)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/game/create')
def create_game():
    game = Game()
    game.current_word = 'hello'
    db.session.add(game)
    db.session.commit()
    return redirect('/game/' + game.game_id)

@routes.route('/game/<code>')
def game(code):
    game = Game.query.filter_by(game_id=code).first()
    if game:
        return render_template('game.html', game_id=code)
    else:
        abort(404)