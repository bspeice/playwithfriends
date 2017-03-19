from unittest import TestCase

from playwithfriends import steam


class SteamTest(TestCase):

    def test_returns_friends_list(self):
        steam_id = '76561198020882912'
        friends = steam.SteamAPI().get_friends(steam_id)
        self.assertTrue(len(friends) > 0)

    def test_I_own_games(self):
        steam_id = '76561198020882912'
        games = steam.SteamAPI().get_games(steam_id)
        self.assertTrue(len(games) > 0)

    def test_Ive_recently_played_games(self):
        steam_id = '76561198020882912'
        games = steam.SteamAPI().get_recent_games(steam_id)
        self.assertTrue(len(games) > 0)

    def test_my_profile_id(self):
        profile_url = 'http://steamcommunity.com/id/fractalize/'
        steam_id = '76561198020882912'

        self.assertEqual(steam.SteamAPI().get_steam64_id(profile_url), steam_id)
