from curry_fp import curry


def test_curry():
    @curry
    def sum_all(a: int, b: int, c: int = 3):
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

    # default args test
    assert sum_all(1)(2)(...) == 6
    assert sum_all(1)(...)(2) == 6
    assert sum_all(...)(1)(2) == 6
    
    assert sum_all(1, 2)(...) == 6
    assert sum_all(...)(1, 2) == 6

    assert sum_all(1, 2, ...) == 6
    assert sum_all(1, ..., 2) == 6
    assert sum_all(..., 1, 2) == 6

    assert sum_all(1)(...)(b=2) == 6
    assert sum_all(...)(1)(b=2) == 6
    assert sum_all(...)(a=1)(b=2) == 6

    assert sum_all(1, ...)(b=2) == 6
    assert sum_all(..., 1)(b=2) == 6
    assert sum_all(..., a=1)(b=2) == 6

    assert sum_all(...)(a=1, b=2) == 6
    assert sum_all(...)(b=2, a=1) == 6

    assert sum_all(..., a=1, b=2) == 6
    assert sum_all(..., 1, b=2) == 6
    assert sum_all(1, ..., b=2) == 6

    assert sum_all(..., 1, 2, 3) == 6

    assert sum_all(...)(1, 2, c=3) == 6
    assert sum_all(...)(1, b=2, c=3) == 6
    assert sum_all(...)(a=1, b=2, c=3) == 6

    assert sum_all(..., 1, 2, c=3) == 6
    assert sum_all(..., 1, b=2, c=3) == 6
    assert sum_all(..., a=1, b=2, c=3) == 6

    assert sum_all(...)(1, 2, c=6) == 9
    assert sum_all(1)(...)(2, c=6) == 9

    assert sum_all(1)(2)(..., c=6) == 9

    assert sum_all(1)(2)(6, ...) == 9
