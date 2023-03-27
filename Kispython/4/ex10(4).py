class StateMachine:
    def __init__(self):
        self.state = 'A'

    def jog(self):
        match(self.state):
            case 'A':
                self.state = 'B'
                return 0
            case 'D':
                self.state = 'B'
                return 5
            case 'E':
                self.state = 'B'
                return 7
        raise MealyError("jog")

    def tweak(self):
        match(self.state):
            case 'B':
                self.state = 'C'
                return 1
            case 'C':
                self.state = 'D'
                return 2
            case 'D':
                self.state = 'E'
                return 3
            case 'E':
                self.state = 'F'
                return 6
        raise MealyError("tweak")

    def cut(self):
        match(self.state):
            case 'D':
                self.state = 'A'
                return 4
            case 'E':
                self.state = 'C'
                return 8
        raise MealyError("cut")


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
    raises(lambda: o.cut(), MealyError)
    raises(lambda: o.tweak(), MealyError)
    assert o.jog() == 0
    assert o.state == 'B'
    raises(lambda: o.cut(), MealyError)
    raises(lambda: o.jog(), MealyError)
    assert o.tweak() == 1
    assert o.state == 'C'
    raises(lambda: o.cut(), MealyError)
    raises(lambda: o.jog(), MealyError)
    assert o.tweak() == 2
    assert o.state == 'D'
    assert o.cut() == 4
    o.state = 'D'
    assert o.jog() == 5
    o.state = 'D'
    assert o.tweak() == 3
    assert o.state == 'E'
    assert o.cut() == 8
    o.state = 'E'
    assert o.jog() == 7
    o.state = 'E'
    assert o.tweak() == 6
    assert o.state == 'F'
    raises(lambda: o.jog(), MealyError)
    raises(lambda: o.cut(), MealyError)
    raises(lambda: o.tweak(), MealyError)
    o.state = 'X'
    raises(lambda: o.jog(), MealyError)
    raises(lambda: o.tweak(), MealyError)
    raises(lambda: o.cut(), MealyError)


test()