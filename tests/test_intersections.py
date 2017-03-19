from unittest import TestCase

from playwithfriends import intersections


class TestIntersections(TestCase):

    def test_xannort_shares_project_cars(self):
        steam_id_left = '76561198020882912'
        steam_id_right = '76561198069992619'

        inter_games = intersections.intersecting_games(
            steamid_left=steam_id_left, steamid_right=steam_id_right
        )

        self.assertIn('Project CARS', inter_games.values())
