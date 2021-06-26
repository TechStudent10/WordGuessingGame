from flask import Blueprint, render_template, redirect, url_for, abort, request, session
from .models import db, User, Game
from flask_socketio import join_room

routes = Blueprint(
    'routes',
    __name__
)

def join_game_func(name, code):
    game = Game.query.filter_by(game_id=code).first()
    if game:
        user = User(username=name, game=game)
        db.session.add(user)
        db.session.commit()

        session['game_id'] = code
        session['user_id'] = user.id
        return user
    return

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/game/create')
def create_game():
    game = Game()
    game.current_word = 'hello'
    db.session.add(game)
    db.session.commit()
    user = join_game_func('Host', game.game_id)
    user.is_host = True
    db.session.commit()
    return redirect('/game')

@routes.route('/game/join', methods=['GET', 'POST'])
def join_game():
    if request.method == 'POST':
        body = request.body

        name = body.get('name')
        code = body.get('code')

        user = join_game_func(name, code)
        if user:
            return redirect(url_for('.game'))
    return render_template('enter_game.html')

@routes.route('/game')
def game():
    if 'game_id' in session:
        code = session['game_id']
        user_id = session['user_id']
        game = Game.query.filter_by(game_id=code).first()
        user = User.query.filter_by(id=user_id).first()
        if game:
            # join_room(game.game_id)
            return render_template(
                'game.html',
                game_id=code,
                user_id=user_id,
                game=game,
                user=user
            )
        else:
            abort(404)
    else:
        return redirect(url_for('.join_game'))