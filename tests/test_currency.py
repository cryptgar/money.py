import pytest

from moneypy import Currency, EUR_CURRENCY, USD_CURRENCY

def test_currency():
    assert EUR_CURRENCY == EUR_CURRENCY
    assert EUR_CURRENCY != USD_CURRENCY