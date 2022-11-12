from MyClass import Book, myFile as file
from os import system as cls


# book1 = Book("Title 1","Author 1","Edition 1",11,1)
# book2 = Book("Title 2","Author 2","Edition 2",22,2)
# book3 = Book("Title 3","Author 3","Edition 3",33,3)


programAuthor: str = "Sioban L." + chr(169)
f = file("Book.si")
books = f.loadToFile()
newBook = Book()

def mainDisplay():
    while True:
        print("+--------------------------+")
        print("|   a: Ajouter un livre    |")
        print("|   b: Preter un livre     |")
        print("|   c: Consulter un livre  |")
        print("|   d: Remetre un livre    |")
        print("|   e: Quiter              |")
        print("+--------------------------+")
        choice = input("Votre choix: ")
        match choice.lower():
            case "a":
                cls("cls")
                addBook()
                # main()
            case "b":
                cls("cls")
                lendBook()
            case "c":
                cls("cls")
                watchBook()
            case "d":
                cls("cls")
                returnBook()
            case "e":
                cls("cls")
                print("Au revoir :)")
                break
        books = f.loadToFile()


def addBook():
    print("+--Ajouter un livre: --+")
    print("|")
    print("+- Titre: ", end="")
    newBook.bookTitle = input()
    print("|")
    print("+- Auteur: ", end="")
    newBook.bookAuthor = input()
    print("|")
    print("+- Edition: ", end="")
    newBook.bookEdition = input()
    print("|")
    print("+- ISNBN: ", end="")
    newBook.bookISBN = input()
    print("|")
    print("+----------------------+")
    newBook.bookID = len(books)
    
    books.append(list(newBook.__str__()))
    f.saveInFile(newBook.__str__())


def lendBook():
    pass


def watchBook():
    pass


def returnBook():
    pass


def main():
    # f.saveInFile(book1.__str__())
    # f.saveInFile(book2.__str__())
    # f.saveInFile(book3.__str__())
    # books.append(f.loadToFile())
    # print(books)
    pass


mainDisplay()

# [
#     'Title 1;Author 1;Edition 1;11;1\n', 
#     'Title 2;Author 2;Edition 2;22;2\n', 
#     'Title 3;Author 3;Edition 3;33;3\n', 
#     'Title 4;Author 4;Edition 4;44;4\n', 
#     'Title 5;Author 5;Edition 5;55;3\n', 
#     'Title 6;Author 6;Edition 6;66;4\n'
# ]