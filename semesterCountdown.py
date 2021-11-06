# keep motivated this semester, display all of your important dates
from datetime import datetime
from typing import Union

# user has to input date in correct format
# we need deadline type: end of semester, test/exam or assignment or other?
#     >>> get_countdown("calico", {"Calico176": ["23 November, 2021", "09 December 2021", "14 December 2021",
#     "19 December 2021"], "JohnD" : ["13 October, 2021", "16 December 2021", })


def get_countdown(deadline: str) -> Union[int, str]:
    """ Return the number of days left until the deadline
    >>> get_countdown("16 December, 2021")
    39
    >>> get_countdown("04 November, 2021")
    'This date has already passed!'
    """
    curr_date = datetime.today()
    d2 = datetime.strptime(deadline, "%d %B, %Y")
    # take care of the case if the date is passed
    diff = (d2 - curr_date).days
    if diff >= 0:
        return diff
    return "This date has already passed!"


def get_all_deadlines(user: str, users: dict[str, list]) -> list[str]:
    """ Return all deadlines for a specific user"""
    deadlines = []
    if len(users[user]) > 0:
        for date in users[user]:
            countdown = get_countdown(date)
            deadlines.append(countdown)
    return deadlines

