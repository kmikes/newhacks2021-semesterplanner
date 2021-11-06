# keep motivated this semester, display all of your important dates
from datetime import datetime
from typing import Union


def get_countdown(deadline: str) -> Union[int, str]:
    """ Return the number of days left until the deadline
    >>> get_countdown("16 December, 2021")
    39
    >>> get_countdown("04 November, 2021")
    0
    """
    curr_date = datetime.today()
    d2 = datetime.strptime(deadline, "%d %B, %Y")
    # take care of the case if the date is passed
    diff = (d2 - curr_date).days
    if diff >= 0:
        return diff
    return "This date has already passed!"

