$(document).ready(function() {
    let socket = io.connect('localhost:5000')
    const game_id = document.getElementById('game_id').innerHTML;
    const log = document.getElementById('log')

    socket.emit('game join', {
        'username': 'b',
        'game_code': game_id
    })


    socket.on('game join', function(json) {
        log.innerHTML += `<p>${json.username} has joined the game.</p>`
        // console.log(`${json.username} has joined the game.`)
    })
})