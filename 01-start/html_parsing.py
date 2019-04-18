from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if (data.isspace()):
            return

        print("Encountered some text data:", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_comment(self, data):
        print("Encountered comment:", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    parser = MyHTMLParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        parser.feed(f.read())


if __name__ == "__main__":
    main()
