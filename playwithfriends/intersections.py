from playwithfriends import steam
from functools import reduce


def intersecting_games(*args):
    api = steam.SteamAPI()

    games_list = [api.get_games(steamid) for steamid in args]
    game_ids = [g.keys() for g in games_list]
    ids_mutual = reduce(lambda l, r: set(l).intersection(r), game_ids)

    return {game_id: games_list[0][game_id] for game_id in ids_mutual}
