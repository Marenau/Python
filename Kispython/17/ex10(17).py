class StateMachine:
    def __init__(self):
        self.state = 'A'

    def reset(self):
        match(self.state):
            case 'A':
                self.state = 'B'
                return 0
            case 'C':
                self.state = 'D'
                return 4
            case 'E':
                self.state = 'C'
                return 8
        raise MealyError("reset")

    def carve(self):
        match(self.state):
            case 'A':
                self.state = 'E'
                return 2
            case 'B':
                self.state = 'C'
                return 3
            case 'D':
                self.state = 'E'
                return 6
            case 'E':
                self.state = 'F'
                return 7
            case 'F':
                self.state = 'G'
                return 9
        raise MealyError("carve")

    def stall(self):
        match(self.state):
            case 'C':
                return 5
            case 'A':
                self.state = 'F'
                return 1
        raise MealyError("stall")


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
    assert o.reset() == 0
    raises(lambda: o.reset(), MealyError)
    assert o.carve() == 3
    raises(lambda: o.carve(), MealyError)
    assert o.stall() == 5
    assert o.reset() == 4
    raises(lambda: o.reset(), MealyError)
    raises(lambda: o.stall(), MealyError)
    assert o.carve() == 6
    raises(lambda: o.stall(), MealyError)
    assert o.reset() == 8
    o.state = 'A'
    assert o.carve() == 2
    assert o.carve() == 7
    raises(lambda: o.reset(), MealyError)
    raises(lambda: o.stall(), MealyError)
    o.state = 'A'
    assert o.stall() == 1
    assert o.carve() == 9
    raises(lambda: o.reset(), MealyError)
    raises(lambda: o.carve(), MealyError)
    raises(lambda: o.stall(), MealyError)
    o.state = 'X'
    raises(lambda: o.reset(), MealyError)
    raises(lambda: o.carve(), MealyError)
    raises(lambda: o.stall(), MealyError)


test()