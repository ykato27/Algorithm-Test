"""
素数を判定するアルゴリズムのpytest

"""
import pytest
from is_prime import is_prime_v3 as is_prime


@pytest.mark.parametrize(('number', 'expected'), [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
])
def test_is_prime_ok(number, expected):
    assert is_prime(number) == expected


@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (4, False),
    (6, False),
    (8, False),
])
def test_is_prime_ng(number, expected):
    assert is_prime(number) == expected