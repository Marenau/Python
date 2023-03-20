class MealyStateMachine:
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
        return MealyError("amass")

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
        return MealyError("view")

    def scale(self):
        match(self.state):
            case 'E':
                self.state = 'F'
                return 5
            case 'F':
                self.state = 'F'
                return 7
        return MealyError("scale")


class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name

    def __str__(self):
        return "MealyError"


def main():
    return MealyStateMachine()


def test():
    o = MealyStateMachine()
    me_a = MealyError("amass")
    me_s = MealyError("scale")
    me_v = MealyError("view")
    assert o.state == 'A'
    assert o.scale().method_name == me_s.method_name
    assert o.view().method_name == me_v.method_name
    assert o.amass() == 0
    assert o.state == 'B'
    assert o.amass().method_name == me_a.method_name
    assert o.scale().method_name == me_s.method_name
    assert o.view() == 1
    assert o.state == 'C'
    assert o.scale().method_name == me_s.method_name
    assert o.view() == 3
    assert o.state == 'F'
    assert o.view().method_name == me_v.method_name
    assert o.scale() == 7
    assert o.state == 'F'
    assert o.amass() == 6
    assert o.state == 'G'
    assert o.scale().method_name == me_s.method_name
    assert o.view() == 9
    assert o.state == 'D'
    assert o.amass().method_name == me_a.method_name
    assert o.scale().method_name == me_s.method_name
    assert o.view() == 4
    assert o.state == 'E'
    assert o.amass().method_name == me_a.method_name
    assert o.view().method_name == me_v.method_name
    assert o.scale() == 5
    assert o.state == 'F'
    assert o.amass() == 6
    assert o.state == 'G'
    assert o.amass() == 8
    assert o.state == 'C'
    assert o.amass() == 2
    assert o.state == 'D'
    o.state = 'X'
    assert o.amass().method_name == me_a.method_name
    assert o.view().method_name == me_v.method_name
    assert o.scale().method_name == me_s.method_name


def test_1():
    o = main()
    print(o.view()) # MealyError
    print(o.amass()) # 0
    print(o.view()) # 1
    print(o.view()) # 3
    print(o.view()) # MealyError
    print(o.amass()) # 6
    print(o.view()) # 9
    print(o.scale()) # MealyError
    print(o.view()) # 4
    print(o.amass()) # MealyError
    print(o.scale()) # 5
    print(o.view()) # MealyError
    print(o.amass()) # 6
    print(o.amass()) # 8
    print(o.amass()) # 2
    print(o.view()) # 4
    print(o.scale()) # 5
    print(o.scale()) # 7
    

def test_2():
    o = main()
    print(o.amass()) # 0
    print(o.view()) # 1
    print(o.amass()) # 2
    print(o.scale()) # MealyError
    print(o.view()) # 4
    print(o.scale()) # 5
    print(o.scale()) # 7
    print(o.amass()) # 6
    print(o.scale()) # MealyError
    print(o.amass()) # 8
    print(o.view()) # 3
    print(o.amass()) # 6
    print(o.view()) # 9
    print(o.view()) # 4
    print(o.scale()) # 5


test()
# test_1()
# test_2()