import datetime


def friday_the_13th():

    my_date = datetime.datetime.now()
    year = my_date.year
    month = my_date.month

    week = my_date.weekday()

    if week == 4:
        return f"{year}-{month:02d}-{13}"

    if my_date.date().day > 13:
        month += 1

    # print(year,month)

    while week != 4:

        if month > 12:
            month = 1
            year += 1

        my_date = datetime.date(year, month, 13)
        week = my_date.weekday()

        month += 1

    print(my_date)

    # print(my_date)
    return f"{year}-{month-1:02d}-{13}"
