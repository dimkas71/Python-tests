import pytest

from core.wallet import People

def test_demo():
    john = People('John')
    paul = People('Paul')

    assert john is People.find('John')
    assert paul is People.find('Paul')
    assert People.find('George') is None