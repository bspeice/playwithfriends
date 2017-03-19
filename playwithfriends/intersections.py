from playwithfriends import steam
from functools import reduce


def intersecting_games(*args):
    api = steam.SteamAPI()

    games_list = [api.get_games(steamid) for steamid in args]
    ids_mutual = reduce(lambda l, r: set(l.keys()).intersection(r.keys()), games_list)

    return {game_id: games_list[0][game_id] for game_id in ids_mutual}
