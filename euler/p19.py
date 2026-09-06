def leap_year(n):
    if (n % 100 == 0 and n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
        return True
    return False


def transdate(n):
    n = n % 7
    match n:
        case 0:
            return "sunday"
        case 1:
            return "monday"
        case 2:
            return "tuesday"
        case 3:
            return "wednesday"
        case 4:
            return "thursday"
        case 5:
            return "friday"
        case 6:
            return "saturday"


# days are 0-6
def first_day_jan(year: int):
    day_zero = 1
    yeardiff = year - 1900
    leaps = yeardiff // 4

    days = 365 * yeardiff + leaps
    diff = days % 7

    if leap_year(year):
        diff -= 1

    return (day_zero + diff) % 7


def sundays_on_one(n: int, leap=0):
    # jan
    return [
        n,
        (n + 3) % 7,
        (n + 3 + leap) % 7,
        (n + 6 + leap) % 7,
        (n + 1 + leap) % 7,
        (n + 4 + leap) % 7,
        (n + 6 + leap) % 7,
        (n + 2 + leap) % 7,
        (n + 5 + leap) % 7,
        (n + 0 + leap) % 7,
        (n + 3 + leap) % 7,
        (n + 5 + leap) % 7,
    ].count(0)

c = 0
for yr in range(1901, 2001):
    fd = first_day_jan(yr)
    c += sundays_on_one(fd, int(leap_year(yr)))
print(c)
