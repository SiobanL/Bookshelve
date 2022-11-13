from MyClass import Book, myFile as file
from os import system as cls


# programAuthor: str = "Sioban L." + chr(169)
f = file("Book.si")
books = f.loadToFile()

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
                cls("cls")
            case "b":
                # cls("cls")
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


def addBook():
    newBook = Book()
    
    print("+--Ajouter un livre: --+")
    print("|")
    newBook.bookTitle = input("+- Titre: ")
    print("|")
    newBook.bookAuthor = input("+- Auteur: ")
    print("|")
    newBook.bookEdition = input("+- Edition: ")
    print("|")
    newBook.bookISBN = input("+- ISNBN: ")
    print("|")
    print("+----------------------+")
    newBook.bookID = len(books)
    
    books.append(newBook.__str__().strip(";"))
    f.saveInFile(newBook.__str__())
    cls("cls")


def lendBook():
    currentBook = Book()
    
    print("+--Preter un livre --+")
    print("|")
    print("+- ID: ",end="")
    search = int(input())
    currentBook.assignProperty(books[search])
    # good /\
    #      ||
    print(not(currentBook.get_state()))
    print(currentBook.get_state())
    #      ||
    # good \/
    books[search] = currentBook.__str__().split(";")
    f.modifyLine(search,currentBook.__str__())


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


def writeThreelines():
    book1 = Book()
    book1.bookTitle = "Title 1"
    book1.bookAuthor = "Author 1"
    book1.bookEdition = "Edition 1"
    book1.bookISBN = 11
    book1.bookID = 0
    f.saveInFile(book1.__str__())
    book1.bookTitle = "Title 2"
    book1.bookAuthor = "Author 2"
    book1.bookEdition = "Edition 2"
    book1.bookISBN = 22
    book1.bookID = 1
    f.saveInFile(book1.__str__())
    book1.bookTitle = "Title 3"
    book1.bookAuthor = "Author 3"
    book1.bookEdition = "Edition 3"
    book1.bookISBN = 33
    book1.bookID = 2
    f.saveInFile(book1.__str__())


# writeThreelines()
# books = f.loadToFile()
mainDisplay()

# [
#     'Title 1;Author 1;Edition 1;11;1\n', 
#     'Title 2;Author 2;Edition 2;22;2\n', 
#     'Title 3;Author 3;Edition 3;33;3\n', 
#     'Title 4;Author 4;Edition 4;44;4\n', 
#     'Title 5;Author 5;Edition 5;55;3\n', 
#     'Title 6;Author 6;Edition 6;66;4\n'
# ]
# Title 1;Author 1;Edition 1;11;1;False
# Title 2;Author 2;Edition 2;22;2;False
