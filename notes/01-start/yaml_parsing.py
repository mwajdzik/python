from yaml import Dumper
from yaml import dump


def main():
    person = {'name': 'Mike', 'age': 25, 'address': {'street': 'Krakowska', 'city': 'Krakow'}}
    output = dump(person, Dumper=Dumper)
    print(output)


if __name__ == "__main__":
    main()
