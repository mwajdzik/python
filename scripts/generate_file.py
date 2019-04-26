def main():
    f = open("file.csv", "w")

    for x in range(ord('A'), ord('Z') + 1):
        for y in range(ord('A'), ord('Z') + 1):
            for z in range(ord('A'), ord('Z') + 1):
                for clazz in range(ord('A'), ord('Z') + 1):
                    origin = chr(x) + chr(y) + chr(z)
                    destination = chr(z) + chr(y) + chr(x)

                    if origin != destination:
                        line = origin + ',' + destination + ',2000-01-01,2020-01-01,' + chr(clazz) + ',100.00,0,100.00'
                        f.write(line + '\n')

    f.close()


if __name__ == "__main__":
    main()
