class Book:
    """
        Class for book. In these class ther is all function we need to manage a library program
    """
    def __init__(self,) -> None:
        self.bookTitle: str = None
        self.bookAuthor: str = None
        self.bookEdition: str = None
        self.bookISBN: int = None
        self.bookID: int = None
        self.bookstate: str = "In bookshelve\n"

    def __str__(self) -> str:
        return str(self.bookTitle) + ";" + str(self.bookAuthor) + ";" + str(self.bookEdition) + ";" + str(self.bookISBN) + ";" + str(self.bookID) + ";" +  str(self.bookstate) #+ "\n"

    def __repr__(self) -> str:
        return f"The title of book is {self.bookTitle} the author is {self.bookAuthor} and it is part of the edition {self.bookEdition} the ISBN is {self.bookISBN} his state is {self.bookstate}\n"

    def get_bookTitle(self)-> str:
        return self.bookTitle

    def get_bookAuthor(self)-> str:
        return self.bookAuthor

    def get_bookEdition(self)-> str:
        return self.bookEdition

    def get_bookISBN(self)-> int:
        return self.bookISBN

    def get_bookID(self)-> int:
        return self.bookID

    def get_state(self)-> str:
        return self.bookstate

    def changeTitle(self,newTitle:str)-> None:
        self.bookTitle = newTitle

    def changeAuthor(self,newAuthor: str)-> None:
        self.bookAuthor = newAuthor

    def changeEdition(self,newEdition: str)-> None:
        self.bookEdition = newEdition

    def changeISBN(self,newISBN:int)-> None:
        self.bookISBN = newISBN

    def changeSate(self,state: str)-> None:
        self.bookstate = state

    def assignProperty(self,strProperty:list)-> None:
        self.bookTitle = strProperty[0]
        self.bookAuthor = strProperty[1]
        self.bookEdition = strProperty[2]
        self.bookISBN = strProperty[3]
        self.bookID = strProperty[4]
        self.bookstate = strProperty[5]


class myFile:
    """
        Class to manage db file of books in a typed file as -.si.
    """
    import os.path

    def __init__(self,FileName) -> None:
        self.FileName = FileName

    def createFile(self)-> None:
        f = open(self.FileName,"x")
        f.close()

    def loadToFile(self)-> list:
        with open(self.FileName,"r") as f:
            rlst: list = []
            for line in f:
                rlst.append(line.split(";"))
        return rlst

    def createOrLoadFile(self)-> list:
        if self.os.path.exists(self.FileName):
            return self.loadToFile()
        else:
            self.createFile()
            return []

    def saveInFile(self,data:str)-> None:
        with open(self.FileName,"a") as f:
            f.write(data)

    def listToStr(self,lst:list) -> str:
        res = ""
        res = res.join(lst)
        return res

    def modifyLine(self,i:int,itemToModify:str)-> None:
        with open(self.FileName,"r+") as f:
            lines = f.readlines()
            lines[i] = itemToModify
            with open(self.FileName,"w") as f2:
                for line in lines:
                    f2.write(self.listToStr(line))