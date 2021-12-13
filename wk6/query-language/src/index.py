from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = query.plays_in("NYR").has_at_least(5, "goals").has_fewer_than(10, "goals") .build()
    # changed the naming to follow pep8

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()