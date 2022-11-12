class Book:
    """
        Class for book. In these class ther is all function we need to manage a library program
    """
    def __init__(self,bookTitle:str,bookAuthor:str,bookEdition:str,bookISBN:int,bookID:int) -> None:
        self.bookTitle: str = bookTitle
        self.bookAuthor: str = bookAuthor
        self.bookEdition: str = bookEdition
        self.bookISBN: int = bookISBN
        self.bookID: int = bookID
    
    def __str__(self) -> str:
        return self.bookTitle + ";" + self.bookAuthor + ";" + self.bookEdition + ";" + str(self.bookISBN) + ";" + str(self.bookID) + "\n"
    
    def __repr__(self) -> str:
        return f"The title of book is {self.bookTitle} the author is {self.bookAuthor} and it is part of the edition {self.bookEdition} the ISBN is {self.bookISBN}\n"
    
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
    
    def changeTitle(self,newTitle:str)-> None:
        self.bookTitle = newTitle
        
    def changeAuthor(self,newAuthor: str)-> None:
        self.bookAuthor = newAuthor

    def changeEdition(self,newEdition: str)-> None:
        self.bookEdition = newEdition

    def changeISBN(self,newISBN:int)-> None:
        self.bookISBN = newISBN
    
    
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
    
    def saveInFile(self,info:str)-> None:
        with open(self.FileName,"a+") as f:
            f.write(info)
            f.close()

    def loadToFile(self)-> list:
        with open(self.FileName,"r+")as f:
            rlst: list = []
            for line in f:
                rlst.append(line)
            f.close()
        return rlst
    
    def createOrLoadFile(self)-> list:
        if self.os.path.exists(self.FileName):
            return self.loadToFile()
        else:
            self.createFile()
            return []