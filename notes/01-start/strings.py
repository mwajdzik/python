from string import Template


def main():
    bytes = 'my string'.encode('utf-8')
    print(bytes)

    unicode = bytes.decode('utf-8')
    print(unicode)

    print('my string'.encode('utf-16'))
    print('my string'.encode('utf-32'))

    print('\n-------------------------------------\n')

    print('Hello {0}!'.format('Maciek'))

    template = Template('You are watching ${title} by ${author}!')
    print(template.substitute(title='Advanced Python', author='Joe'))


if __name__ == '__main__':
    main()
