def my_function(number=1):
    print("the passed number is " + str(number))


def multi_add(*args):
    result = 0

    for x in args:
        result = result + x

    return result


def fun_arguments(arg1, arg2, *, suppress=False):
    print(arg1, arg2, suppress)


def power(num, x=1):
    result = 1

    for i in range(x):
        result = result * num

    return result


def compare(x, y):
    if (x < y):
        str1 = "x is less than y"
    elif (x == y):
        str1 = "x is same as y"
    else:
        str1 = "x is greater than y"

    str2 = "x is less than y" if (x < y) \
        else "x is greater than or equal to y"

    print(str1)
    print(str2)


def loops():
    x = 0

    while (x < 3):
        print(x)
        x = x + 1

    for x in range(5, 7):
        print(x)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    for x in range(5, 10):
        if x == 7:
            break

        if x % 2 == 0:
            continue

        print(x)

    for i, d in enumerate(days):
        print(i, d)


def main():
    print("hello world!")

    my_function()
    my_function(23)
    my_function(power(2, 6))
    my_function(multi_add(1, 2, 3, 4, 5, 6, 7, 8))

    fun_arguments(23, 'world')
    fun_arguments(23, 'world', suppress=True)

    compare(23, 36)

    loops()


if __name__ == "__main__":
    main()
