from flask_socketio import SocketIO, emit, join_room, leave_room

socketio = SocketIO(cors_allowed_origins='*')

@socketio.on('game join')
def join_game(json):
    game_code = json.get('game_code')
    join_room(game_code)
    emit('game join', json, room=game_code, broadcast=True)