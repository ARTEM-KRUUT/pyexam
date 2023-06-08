class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def put(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'F':
            self.state = 'G'
            return 6
        if self.state == 'H':
            self.state = 'C'
            return 11
        raise MealyError('put')

    def group(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'G'
            return 3
        if self.state == 'F':
            self.state = 'H'
            return 7
        if self.state == 'G':
            self.state = 'D'
            return 9
        raise MealyError('group')

    def start(self):
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 5
        if self.state == 'H':
            self.state = 'E'
            return 10
        raise MealyError('start')

    def slur(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'G':
            self.state = 'H'
            return 8
        raise MealyError('slur')


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()

    raises(o.group, MealyError)
    raises(o.start, MealyError)
    raises(o.slur, MealyError)
    assert o.put() == 0  # A -> B

    raises(o.put, MealyError)
    raises(o.start, MealyError)
    raises(o.slur, MealyError)
    assert o.group() == 1  # B -> C

    raises(o.start, MealyError)
    raises(o.put, MealyError)
    assert o.group() == 3  # C -> G

    o.state = 'C'

    assert o.slur() == 2  # C -> D

    raises(o.put, MealyError)
    raises(o.group, MealyError)
    raises(o.slur, MealyError)
    assert o.start() == 4  # D -> E

    raises(o.put, MealyError)
    raises(o.group, MealyError)
    raises(o.slur, MealyError)
    assert o.start() == 5  # E -> F

    raises(o.start, MealyError)
    raises(o.slur, MealyError)
    assert o.group() == 7  # F -> H

    o.state = 'F'

    assert o.put() == 6  # F -> G

    raises(o.put, MealyError)
    raises(o.start, MealyError)
    assert o.group() == 9  # G -> D

    o.state = 'G'

    assert o.slur() == 8  # G -> H

    raises(o.group, MealyError)
    raises(o.slur, MealyError)
    assert o.start() == 10  # H -> E

    o.state = 'H'

    assert o.put() == 11  # H -> C
