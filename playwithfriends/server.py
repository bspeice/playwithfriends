from bottle import route, run, request

from playwithfriends.templates import render_template
from playwithfriends.steam import SteamAPI
from playwithfriends.intersections import intersecting_games


@route('/')
def index():
    return render_template('index.html')


@route('/get_friends')
def get_friends():
    api = SteamAPI()
    steam64_id = api.get_steam64_from_profile(request.params['profile_url'])
    friends_ids = api.get_friends_ids(steam64_id)

    return api.get_player_names(friends_ids)


@route('/get_games')
def get_games():
    player_ids = request.params['player_ids'].split(',')
    inter_games = intersecting_games(*player_ids)

    return inter_games


def main():
    run(host='localhost', port=8000)

if __name__ == '__main__':
    main()
