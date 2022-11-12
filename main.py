from MyClass import Book, myFile as file


programAuthor: str = "Sioban L." + chr(169)
book = Book("Title 1","Author 1","Edition 1",11,1)


def main():
    f = file("Book.si")
    newbook = f.createOrLoadFile()
    test = book.__str__()
    f.saveInFile(test+"\n")
    print(test)


main()