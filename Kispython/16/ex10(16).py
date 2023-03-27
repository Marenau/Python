class StateMachine:
    def __init__(self):
        self.state = 'A'

    def amass(self):
        match(self.state):
            case 'A':
                self.state = 'B'
                return 0
            case 'C':
                self.state = 'D'
                return 2
            case 'F':
                self.state = 'G'
                return 6
            case 'G':
                self.state = 'C'
                return 8
        raise MealyError("amass")

    def view(self):
        match(self.state):
            case 'B':
                self.state = 'C'
                return 1
            case 'C':
                self.state = 'F'
                return 3
            case 'D':
                self.state = 'E'
                return 4
            case 'G':
                self.state = 'D'
                return 9
        raise MealyError("view")

    def scale(self):
        match(self.state):
            case 'E':
                self.state = 'F'
                return 5
            case 'F':
                self.state = 'F'
                return 7
        raise MealyError("scale")


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
    raises(lambda: o.scale(), MealyError)
    raises(lambda: o.view(), MealyError)
    assert o.amass() == 0
    assert o.state == 'B'
    raises(lambda: o.amass(), MealyError)
    raises(lambda: o.scale(), MealyError)
    assert o.view() == 1
    assert o.state == 'C'
    raises(lambda: o.scale(), MealyError)
    assert o.view() == 3
    assert o.state == 'F'
    raises(lambda: o.view(), MealyError)
    assert o.scale() == 7
    assert o.state == 'F'
    assert o.amass() == 6
    assert o.state == 'G'
    raises(lambda: o.scale(), MealyError)
    assert o.view() == 9
    assert o.state == 'D'
    raises(lambda: o.amass(), MealyError)
    raises(lambda: o.scale(), MealyError)
    assert o.view() == 4
    assert o.state == 'E'
    raises(lambda: o.amass(), MealyError)
    raises(lambda: o.view(), MealyError)
    assert o.scale() == 5
    assert o.state == 'F'
    assert o.amass() == 6
    assert o.state == 'G'
    assert o.amass() == 8
    assert o.state == 'C'
    assert o.amass() == 2
    assert o.state == 'D'
    o.state = 'X'
    raises(lambda: o.amass(), MealyError)
    raises(lambda: o.view(), MealyError)
    raises(lambda: o.scale(), MealyError)


test()