from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query=All()):
        self.matcher = query

    def build(self):
        return self.matcher

    def plays_in(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))
