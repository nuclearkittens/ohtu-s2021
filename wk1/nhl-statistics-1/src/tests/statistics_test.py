import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        reader = PlayerReaderStub()
        self.plrs = reader.get_players()
        self.stats = Statistics(reader)

    def test_init_ok(self):
        plrs = [plr.name for plr in self.stats._players]
        expected = [plr.name for plr in self.plrs]
        self.assertEqual(plrs, expected)

    def test_search_returns_player(self):
        name = 'Kurri'
        self.assertEqual(self.stats.search(name).name, name)

    def test_search_returns_none(self):
        self.assertIsNone(self.stats.search('UKK'))

    def test_returns_right_team_amt(self):
        edm = self.stats.team('EDM')
        pit = self.stats.team('PIT')
        det = self.stats.team('DET')
        no_team = self.stats.team('XYZ')
        self.assertEqual(
            [len(edm), len(pit), len(det), len(no_team)],
            [3, 1, 1, 0]
        )

    def test_return_right_team_plr(self):
        pit = self.stats.team('PIT')
        self.assertEqual(str(pit[-1]), str(self.plrs[1]))

    def test_top_score_first(self):
        top = self.stats.top_scorers(1)[0]
        self.assertEqual(top.name, 'Gretzky')

    def test_top_score_last(self):
        last = self.stats.top_scorers(5)[-1]
        self.assertEqual(last.name, 'Semenko')