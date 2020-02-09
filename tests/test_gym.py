import pytest

from core.gym import to_time, InvalidArgumentException

def test_format_time():
    assert "08:24:30" == to_time(8,24,30)
    assert "12:03:04" == to_time(12, 3, 4)
    assert "11:02:00" == to_time(11, 2, 0)

def test_should_raise_InvalidArgumentException_if_hours_no_correct():
    with pytest.raises(InvalidArgumentException):
        to_time(25, 12, 24)

def test_should_raise_InvalidArgumentException_if_minutes_no_correct():
    with pytest.raises(InvalidArgumentException):
        to_time(22, 61, 24)                

def test_should_raise_InvalidArgumentException_if_seconds_no_correct():
    with pytest.raises(InvalidArgumentException):
        to_time(22, 4, 60)

@pytest.mark.parametrize("hours, minutes, seconds, expected",
        [
                (7, 23, 44, "07:23:44"),
                (0, 0, 0, "00:00:00"),
                (17, 5, 2, "17:05:02"),
                (23, 59, 59, "23:59:59")
        ]
)
def test_bulk_with_parametrize(hours, minutes, seconds, expected):
        assert expected == to_time(hours, minutes, seconds)
