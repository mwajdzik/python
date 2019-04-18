import calendar
from datetime import date, timedelta
from datetime import datetime


def main():
    today = date.today()
    print("Today's date is ", today)
    print("Date Components: ", today.day, today.month, today.year)

    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

    print("Today's Weekday is ", today.weekday())
    print("Which is a " + days[today.weekday()])

    today = datetime.now()
    print("The current date and time is ", today)

    t = datetime.time(datetime.now())
    print("The current time is ", t)

    print("\n-------------------------------------\n")

    print(today.strftime("The current year is: %Y"))
    print(today.strftime("%a, %d %B, %y"))
    print(today.strftime("Locale date and time: %c"))
    print(today.strftime("Locale date: %x"))
    print(today.strftime("Locale time: %X"))
    print(today.strftime("Current time: %I:%M:%S %p"))
    print(today.strftime("24-hour time: %H:%M"))

    print("\n-------------------------------------\n")

    print("today is: " + str(datetime.now()))
    print("one year from now it will be: " + str(datetime.now() + timedelta(days=365)))
    print("in two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks=2, days=3)))
    print("one week ago it was " + (datetime.now() - timedelta(weeks=1)).strftime("%A %B %d, %Y"))

    print()
    print("How many days until April Fools' Day?")

    today = date.today()
    first_of_april = date(today.year, 4, 1)

    if first_of_april < today:
        print("April Fool's day already went by %d days ago" % ((today - first_of_april).days))
        first_of_april = first_of_april.replace(year=today.year + 1)

    print("It's just %d days until next April Fools' Day!" % (first_of_april - today).days)

    print("\n-------------------------------------\n")

    c = calendar.TextCalendar(calendar.MONDAY)
    print(c.formatmonth(2017, 1, 0, 0))

    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    print(hc.formatmonth(2017, 1))

    # zeroes mean that the day of the week is in an overlapping month
    for i in c.itermonthdays(2017, 8):
        print(i)

    for name in calendar.month_name:
        print(name)

    for day in calendar.day_name:
        print(day)

    print("Team meetings will be on the first Friday of every month:")
    for m in range(1, 13):
        cal = calendar.monthcalendar(2017, m)

        weekone = cal[0]
        weektwo = cal[1]

        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]

        print("%10s %2d" % (calendar.month_name[m], meetday))


if __name__ == "__main__":
    main()
