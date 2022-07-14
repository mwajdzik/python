def main():
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    # Perform a mapping and filter function on a list
    even_squared = list(map(lambda e: e ** 2, filter(lambda e: 4 < e < 16, evens)))
    print(even_squared)

    # Derive a new list of numbers frm a given list
    even_squared = [e ** 2 for e in evens if 4 < e < 16]
    print(even_squared)

    # ---

    c_temps = [0, 12, 34, 100]

    temp_dict = {t: ((t * 9 / 5) + 32) for t in c_temps if (t < 100)}
    print(temp_dict)
    print(temp_dict[12])

    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}
    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)

    # ---

    c_temps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    ftemps1 = [(t * 9 / 5) + 32 for t in c_temps]
    ftemps2 = {(t * 9 / 5) + 32 for t in c_temps}

    print(ftemps1)
    print(ftemps2)

    temp = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in temp if not c.isspace()}
    print(chars)


if __name__ == '__main__':
    main()
