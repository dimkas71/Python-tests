def to_time(hours, minutes, seconds):
    
    if (hours < 0 or hours > 23):
        raise InvalidArgumentException("Non proper hours value")

    if (minutes < 0 or minutes > 59):
        raise InvalidArgumentException("Non proper minutes value")  

    if (seconds < 0 or seconds > 59):
        raise InvalidArgumentException("Non proper seconds value")

    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)


class InvalidArgumentException(Exception):
    pass