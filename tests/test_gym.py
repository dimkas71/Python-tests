import pytest

from core.gym import to_time

def test_format_time():
    assert "08:24:30" == to_time(8,24,30)
    assert "12:03:04" == to_time(12, 3, 4)
    assert "11:02:00" == to_time(11, 2, 0)


