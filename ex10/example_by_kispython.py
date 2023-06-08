class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    # Определяем рёбра с названием "spin"
    # ( после чёрточки - возвращаемое значение)
    def spin(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'B':
            self.state = 'E'
            return 3
        if self.state == 'E':
            self.state = 'F'
            return 6
        raise MealyError('spin')

    # Определяем рёбра с названием "punch"
    # ( после чёрточки - возвращаемое значение)
    def punch(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'E':
            self.state = 'A'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('punch')

    # Определяем рёбра с названием "stand"
    # ( после чёрточки - возвращаемое значение)
    def stand(self):
        if self.state == 'B':
            self.state = 'G'
            return 2
        if self.state == 'E':
            self.state = 'G'
            return 8
        raise MealyError('stand')


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
    # Проходимся по рёбрам первый раз
    o = main()
    assert o.spin() == 0
    assert o.punch() == 1
    assert o.spin() == 4
    assert o.spin() == 5
    assert o.punch() == 7
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.spin() == 6
    assert o.punch() == 9
    # Вызываем заново проход
    # Проходимся по недостающим рёбрам
    o = main()
    assert o.spin() == 0
    assert o.stand() == 2
    # Вызываем заново проход
    # Проходимся по недостающим рёбрам
    o = main()
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.stand() == 8
    raises(lambda: o.stand(), MealyError)
    raises(lambda: o.punch(), MealyError)
    raises(lambda: o.spin(), MealyError)
