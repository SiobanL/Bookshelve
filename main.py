from MyClass import Book, myFile as file


programAuthor: str = "Sioban L." + chr(169)
book1 = Book("Title 1","Author 1","Edition 1",11,1)
book2 = Book("Title 2","Author 2","Edition 2",22,2)
book3 = Book("Title 3","Author 3","Edition 3",33,3)
f = file("Book.si")

def display():
    while True:
        print("+--------------------------+")
        print("|   a: Ajouter un livre    |")
        print("|   b: Preter un livre     |")
        print("|   c: Consulter un livre  |")
        print("|   d: Remetre un livre    |")
        print("|   e: Quiter              |")
        print("+--------------------------+")
        choice = input("Votre choix: ...")
        match choice.lower:
            case "a":
                addbook()
            case "b":
                lendbook()
            case "c":
                watchBook()
            case "d":
                returnBook()
            case "e":
                break


def addbook():
    pass


def lendbook():
    pass


def watchBook():
    pass


def returnBook():
    pass


def main():
    f.saveInFile(book1.__str__())
    f.saveInFile(book2.__str__())
    f.saveInFile(book3.__str__())
    newbook = f.createOrLoadFile()
    print(newbook)


main()