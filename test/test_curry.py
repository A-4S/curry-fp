from currypy import curry


def test_curry():
    @curry
    def sum_all(a: int, b: int, c: int):
        return a + b + c

    # args test
    assert sum_all(1)(2)(3) == 6
    assert sum_all(1, 2)(3) == 6
    assert sum_all(1, 2, 3) == 6

    # kwargs test
    assert sum_all(a=1)(b=2)(c=3) == 6
    assert sum_all(b=1)(c=2)(a=3) == 6
    assert sum_all(c=1)(a=2)(b=3) == 6

    # mixed test
    assert sum_all(1)(2)(c=3) == 6
    assert sum_all(1, b=2)(c=3) == 6
    assert sum_all(a=1, b=2, c=3) == 6
