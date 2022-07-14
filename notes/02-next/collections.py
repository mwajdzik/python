import collections
import string
from collections import namedtuple, defaultdict, Counter, OrderedDict


def main():
    my_list = [1, 4, 7, 7, 7]
    my_tuple = (2, 4, 5)
    my_set = {7, 3, 4}
    my_dict = {'a': 1, 'b': 2}

    print(my_list)
    print(my_tuple)
    print(my_set)
    print(my_dict)

    for n in my_list:
        pass

    for k in my_dict.keys():
        pass

    # ---
    # NAMED TUPLE:

    point = namedtuple('point', 'x y')
    p1 = point(10, 20)
    p2 = point(30, 40)
    print(p1.x, p1.y, p2.x, p2.y)

    print(p1)
    p1 = p1._replace(x=100)
    print(p1)

    # ---
    # DEFAULT DICT

    # dict with a default value provided by the constructor int (0)
    counter = defaultdict(int)
    for n in my_list:
        counter[n] += 1

    print(counter)

    # ---
    # COUNTER

    counter = Counter(my_list)
    print('Number of 7s:', counter[7])
    print('Count of all numbers:', sum(counter.values()))

    counter.update(Counter(my_tuple))
    print('Count of all numbers:', sum(counter.values()))

    counter.subtract(Counter(my_set))
    print(counter.most_common(3))

    # ---
    # ORDERED DICT

    teams = [
        ('Royals', (18, 12)),
        ('Rockets', (24, 6)),
        ('Cardinals', (20, 10)),
        ('Dragons', (22, 8)),
        ('Kings', (15, 15)),
        ('Chargers', (20, 10)),
        ('Jets', (16, 14)),
        ('Warriors', (25, 5))
    ]

    teams = sorted(teams, key=lambda t: t[1][0], reverse=True)
    teams = OrderedDict(teams)
    print(teams)

    tm, wl = teams.popitem(False)
    print('Top team: ', tm, wl)

    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    print('Equality test: ',
          OrderedDict({'a': 1, 'b': 2, 'c': 3}) ==
          OrderedDict({'a': 1, 'c': 3, 'b': 2}))

    # ---
    # DEQUE - double ended queue (deck)

    d = collections.deque(string.ascii_lowercase)
    print('Item count: ' + str(len(d)))

    d.pop()
    d.popleft()
    d.append('2')
    d.appendleft('1')
    print(d)

    d.rotate(15)
    print(d)


if __name__ == '__main__':
    main()
