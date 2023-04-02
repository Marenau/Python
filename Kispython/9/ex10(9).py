class StateMachine:
    def __init__(self):
        self.state = 'A'

    def shift(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 3
        raise MealyError('shift')

    def cull(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'A'
            return 7
        raise MealyError('cull')

    def hurry(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'C':
            self.state = 'A'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            return 8
        raise MealyError('hurry')


class MealyError(Exception):
    pass


def main():
    return StateMachine()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.state == 'A'
    raises(lambda: o.cull(), MealyError)
    assert o.shift() == 0
    raises(lambda: o.shift(), MealyError)
    raises(lambda: o.hurry(), MealyError)
    assert o.cull() == 2
    raises(lambda: o.cull(), MealyError)
    assert o.hurry() == 4
    assert o.hurry() == 1
    raises(lambda: o.cull(), MealyError)
    o.state = 'C'
    assert o.shift() == 3
    raises(lambda: o.shift(), MealyError)
    assert o.hurry() == 5
    raises(lambda: o.shift(), MealyError)
    raises(lambda: o.hurry(), MealyError)
    assert o.cull() == 6
    raises(lambda: o.shift(), MealyError)
    assert o.hurry() == 8
    assert o.cull() == 7
    o.state = 'X'
    raises(lambda: o.shift(), MealyError)
    raises(lambda: o.cull(), MealyError)
    raises(lambda: o.hurry(), MealyError)


test()