import itertools


def filter_func(x):
    return x % 2 == 1


def map_func(x):
    return x * x


def main():
    my_list = [9, 1, 4, 0, 8, 2, 5, 3, 7, 6]

    print(any(my_list))
    print(all(my_list))
    print(min(my_list))
    print(max(my_list))
    print(sum(my_list))

    # ---

    days_en = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    days_pl = ['Niedziela', 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota']

    i = iter(days_en)
    print(next(i))
    print(next(i))
    print(next(i))

    for i, m in enumerate(days_pl, start=1):
        print(i, m)

    for pl, en in zip(days_pl, days_en):
        print(pl, 'is', en)

    for i, m in enumerate(zip(days_pl, days_en), start=1):
        print(i, m[0], m[1])

    # ---

    odd_numbers = list(filter(filter_func, my_list))
    print(odd_numbers)

    even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
    print(even_numbers)

    squared_numbers = list(map(map_func, my_list))
    print(squared_numbers)

    # ---

    names = ['Maciek', 'Magda', 'Kuba']

    i = itertools.cycle(names)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

    i = itertools.count(100, 10)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

    acc = itertools.accumulate(my_list, max)
    print(list(acc))

    ch = itertools.chain('ABCD', '1234')
    print(list(ch))

    print()
    print(my_list)
    print(list(itertools.dropwhile(filter_func, my_list)))
    print(list(itertools.takewhile(filter_func, my_list)))


if __name__ == "__main__":
    main()
