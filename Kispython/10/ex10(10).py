class StateMachine:
    def __init__(self):
        self.state = 'A'

    def edit(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            return 7
        elif self.state == 'E':
            self.state = 'F'
            return 8
        raise MealyError('edit')

    def tail(self):
        if self.state == 'C':
            return 5
        elif self.state == 'A':
            self.state = 'E'
            return 2
        raise MealyError('tail')

    def spawn(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        if self.state == 'D':
            self.state = 'E'
            return 6
        raise MealyError('spawn')


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
    assert o.edit() == 0
    raises(lambda: o.tail(), MealyError)
    raises(lambda: o.spawn(), MealyError)
    assert o.edit() == 3
    raises(lambda: o.spawn(), MealyError)
    assert o.tail() == 5
    assert o.edit() == 4
    raises(lambda: o.tail(), MealyError)
    assert o.edit() == 7
    assert o.spawn() == 6
    raises(lambda: o.tail(), MealyError)
    raises(lambda: o.spawn(), MealyError)
    assert o.edit() == 8
    raises(lambda: o.edit(), MealyError)
    raises(lambda: o.tail(), MealyError)
    raises(lambda: o.spawn(), MealyError)
    o.state = 'A'
    assert o.tail() == 2
    o.state = 'A'
    assert o.spawn() == 1
    o.state = 'X'
    raises(lambda: o.edit(), MealyError)
    raises(lambda: o.tail(), MealyError)
    raises(lambda: o.spawn(), MealyError)


test()