class StateMachine:
    def __init__(self):
        self.state = 'A'

    def show(self):
        match(self.state):
            case 'A':
                self.state = 'B'
                return 0
            case 'B':
                self.state = 'E'
                return 3
            case 'C':
                self.state = 'D'
                return 4
            case 'D':
                self.state = 'D'
                return 6
        raise MealyError("show")

    def cue(self):
        match(self.state):
            case 'A':
                self.state = 'F'
                return 1
            case 'B':
                self.state = 'C'
                return 2
            case 'D':
                self.state = 'E'
                return 5
            case 'E':
                self.state = 'F'
                return 7
            case 'F':
                self.state = 'C'
                return 8
        raise MealyError("cue")


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
    assert o.show() == 0
    assert o.cue() == 2
    raises(lambda: o.cue(), MealyError)
    assert o.show() == 4
    assert o.show() == 6
    assert o.cue() == 5
    raises(lambda: o.show(), MealyError)
    assert o.cue() == 7
    raises(lambda: o.show(), MealyError)
    assert o.cue() == 8
    o.state = 'A'
    assert o.cue() == 1
    o.state = 'B'
    assert o.show() == 3
    o.state = 'X'
    raises(lambda: o.cue(), MealyError)
    raises(lambda: o.show(), MealyError)


test()