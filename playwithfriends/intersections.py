from playwithfriends import steam


def intersecting_games(steamid_left, steamid_right):
    api = steam.SteamAPI()

    games_left = api.get_games(steamid_left)
    games_right = api.get_games(steamid_right)

    ids_mutual = set(games_left.keys()).intersection(games_right.keys())

    return {game_id: games_left[game_id] for game_id in ids_mutual}
