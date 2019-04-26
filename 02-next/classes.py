from enum import Enum, unique, auto


# ENUM
@unique
class Fruit(Enum):
    APPLE = 1
    ORANGE = 2
    TOMATO = 3
    PEAR = auto()


# STRING VALUES
class Person():
    def __init__(self):
        self.fname = 'Joe'
        self.lname = 'Marini'
        self.age = 25

    def __repr__(self):
        return '<Person Class - fname:{0}, lname:{1}, age{2}>' \
            .format(self.fname, self.lname, self.age)

    # use str for a more human-readable string
    def __str__(self):
        return 'Person ({0} {1} is {2})' \
            .format(self.fname, self.lname, self.age)

    def __bytes__(self):
        val = 'Person:{0}:{1}:{2}'.format(self.fname, self.lname, self.age)
        return bytes(val.encode('utf-8'))


# COMPUTED ATTRIBUTES
class Color():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return '#{0:02x}{1:02x}{2:02x}'.format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # use dir to list the available properties
    def __dir__(self):
        return ('rgbcolor', 'hexcolor')


# OBJECTS OPERATIONS
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


# OBJECTS COMPARISON
class Employee():
    def __init__(self, fname, lname, level, yrs_service):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrs_service

    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority

        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority

        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority

        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority

        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level


def main():
    print(Fruit.APPLE, type(Fruit.APPLE), repr(Fruit.APPLE))
    print(Fruit.PEAR, type(Fruit.PEAR), repr(Fruit.PEAR))

    my_fruit = {Fruit.PEAR: 'gruszka'}
    print(my_fruit)

    # ---
    person = Person()
    print(repr(person))
    print(str(person))
    print('Formatted: {0}'.format(person))
    print(bytes(person))

    # ---
    cls1 = Color()
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    print(cls1.red)
    print(dir(cls1))

    # ---
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    print(p1 + p2)
    print(p2 - p1)

    p1 += p2
    print(p1)

    # ---
    dept = [
        Employee("Tim", "Sims", 5, 9),
        Employee("John", "Doe", 4, 12),
        Employee("Jane", "Smith", 6, 6),
        Employee("Rebecca", "Robinson", 5, 13),
        Employee("Tyler", "Durden", 5, 12)
    ]

    print('Who\'s more senior?')
    print(bool(dept[0] > dept[2]))
    print(bool(dept[4] < dept[3]))

    print('Sorted employees:')
    for emp in sorted(dept):
        print('\t', emp.lname)


if __name__ == '__main__':
    main()
