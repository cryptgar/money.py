import pytest

from moneypy import Money, EUR_CURRENCY, IQD_CURRENCY


def test_money():
    m1 = Money(EUR_CURRENCY)

    m1.add(4, 2)

    assert m1.amount == 402
    assert m1.currency == EUR_CURRENCY


def test_money_str():
    m = Money(EUR_CURRENCY)
    m2 = Money(IQD_CURRENCY)

    m.add(4, 234)
    m2.add(2, 432)

    assert m.__str__() == "6.34 EUR"
    assert m2.__str__() == "2.432 IQD"


def test_money_currency_mismatch():
    m = Money(EUR_CURRENCY)
    m2 = Money(IQD_CURRENCY)

    with pytest.raises(ValueError):
        m += m2


def test_money_addition():
    a = Money(EUR_CURRENCY)
    b = Money(EUR_CURRENCY)

    a.add(2, 20)
    assert a.amount == 220

    b.add(0, 230)
    assert b.amount == 230

    a += b

    assert a.amount == 450


def test_money_sub():
    a = Money(EUR_CURRENCY)
    b = Money(EUR_CURRENCY)

    a.add(2, 20)
    assert a.amount == 220

    b.add(0, 230)
    assert b.amount == 230

    a -= b

    assert a.amount == -10

    a.sub(0, 5)

    assert a.amount == -15


def test_money_mul():
    a = Money(EUR_CURRENCY, 400)

    a.mul(2)

    assert a.amount == 800

    a *= 2

    assert a.amount == 1600


def test_money_div():
    a = Money(EUR_CURRENCY, 400)

    a.div(2)

    assert a.amount == 200

    a /= 2

    assert a.amount == 100

    a //= 2

    assert a.amount == 50


def test_money_invert():
    a = Money(EUR_CURRENCY, 400)

    a = ~a

    assert a.amount == -401


def test_money_pow():
    a = Money(EUR_CURRENCY, 400)

    a = a ** 2

    assert a.amount == 160000


def test_money_mod():
    a = Money(EUR_CURRENCY, 400)

    a = a % 2

    assert a.amount == 0


def test_money_equality():
    a = Money(EUR_CURRENCY, 200)
    b = Money(EUR_CURRENCY, 300)
    c = Money(EUR_CURRENCY, 300)

    assert a < b
    assert b > a
    assert a != b
    assert c == b


def test_money_tofloat():
    a = Money(EUR_CURRENCY, 253)
    b = Money(EUR_CURRENCY, 25233)
    c = Money(EUR_CURRENCY, -3456)
    assert a.to_float() == pytest.approx(2.53)
    assert b.to_float() == pytest.approx(252.33)
    assert c.to_float() == pytest.approx(-34.56)


def test_money_units():
    a = Money(EUR_CURRENCY, 253)
    c = Money(EUR_CURRENCY, -3456)

    assert a.units() == 2
    assert a.cents() == 53

    assert c.units() == -34
    assert c.cents() == 56
