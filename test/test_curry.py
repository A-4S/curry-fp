from currypy import curry


def test_curry():
    @curry
    def sum_all(a: int, b: int, c: int):
        return a + b + c

    assert sum_all(1)(2)(3) == 6
    assert sum_all(1, 2)(3) == 6
    assert sum_all(1, 2, 3) == 6
