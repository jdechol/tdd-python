from money import Money


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) == Money.franc(5)
    assert Money.franc(5) != Money.franc(6)
    assert Money.dollar(2) != Money.franc(2)


def test_multiplication():
    five = Money.dollar(5)
    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)

    five = Money.franc(5)
    assert five.times(2) == Money.franc(10)
    assert five.times(3) == Money.franc(15)
