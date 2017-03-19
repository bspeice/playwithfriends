import requests
from enum import Enum
from os import path
from copy import deepcopy
import logging
from bs4 import BeautifulSoup


_base_url = 'http://api.steampowered.com'


class WebAPI(Enum):
    news = 'ISteamNews'
    user_stats = 'ISteamUserStats'
    user = 'ISteamUser'
    player_service = 'IPlayerService'


class SteamAPI(object):

    def __init__(self):
        file_dir = path.abspath(path.dirname(__file__))
        api_file = path.join(file_dir, 'api_key.txt')
        with open(api_file, 'r') as handle:
            self.api_key = handle.read().strip()

    def _make_request(self, api, function, version, extra_params):
        full_params = deepcopy(extra_params)
        full_params['key'] = self.api_key
        request_url = '/'.join([_base_url, api.value, function, version]) + '/'
        logging.debug('GET: {}'.format(request_url))
        response = requests.get(
            request_url,
            params=full_params
        )
        logging.debug('Return code: {}'.format(response.status_code))
        return response.json()

    def get_friends_ids(self, steam_id):
        """
        Return the steam_id's of all users this user is friends with

        :param steam_id: ID for the user we are looking up
        :type steam_id: str
        :return: List of all id's this user is friends with
        :rtype: list[str]
        """
        friends_list = self._make_request(
            WebAPI.user,
            'GetFriendList',
            'v0001',
            {
                'steamid': steam_id
            })['friendslist']

        return [
            f['steamid'] for f in friends_list['friends']
        ]

    def get_games(self, steam_id):
        """
        Get all the appid's for a user that they can play. Structure
        for return is a dict with `appid: name` values.

        :param steam_id:
        :return: List of appid's
        :rtype: dict
        """
        games = self._make_request(
            WebAPI.player_service,
            'GetOwnedGames',
            'v0001',
            {
                'steamid': steam_id,
                'include_appinfo': 1,
                'include_played_free_games': 1
            })['response']['games']

        return {g['appid']: g['name'] for g in games}

    def get_recent_games(self, steam_id):
        """
        Get all appid's that a user has recently played

        :param steam_id: ID for a steam user
        :type steam_id: str
        :return: List of appids the user has recently played
        """
        games = self._make_request(
            WebAPI.player_service,
            'GetRecentlyPlayedGames',
            'v0001',
            {
                'steamid': steam_id
            }
        )['response']['games']

        return [g['appid'] for g in games]

    def get_player_summary(self, steam_ids):

        return self._make_request(
            WebAPI.user,
            'GetPlayerSummaries',
            'v0002',
            {
                'steamids': ','.join(steam_ids)
            }
        )['response']['players']

    def get_player_names(self, steam_ids):
        """

        :param steam_ids:
        :return: Persona names for all id's supplied
        :rtype: list
        """
        players = self.get_player_summary(steam_ids)
        return {p['steamid']: p['personaname'] for p in players}

    def get_steam64_from_profile(self, profile_url):
        """
        Get the Steam64 ID for a user, given their profile URL.
        This is by far and above the mostly likely piece of code
        to break, be careful in the future.

        :param profile_url: Steam community profile URL
        :type profile_url: str
        :return: Steam64 ID
        :rtype: str
        """
        profile_html = requests.get(profile_url)

        soup = BeautifulSoup(profile_html.content, 'lxml')
        comment_paging = soup.find('div', {'class': 'commentthread_paging'})
        steamid = comment_paging.attrs['id'].split('_')[2]
        return steamid
