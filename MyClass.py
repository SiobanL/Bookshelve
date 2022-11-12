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
        bookTitlestr = self.bookTitle
        bookAuthorstr = self.bookAuthor
        bookEditionstr = self.bookEdition
        bookISBNstr = str(self.bookISBN)
        bookIDstr = str(self.bookID)
        return bookTitlestr +":"+ bookAuthorstr +":"+ bookEditionstr +":"+ bookISBNstr +":"+ bookIDstr

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
    
    
class myFile:
    """
        Class to manage db file of books
    """
    import os
    
    def __init__(self,FileName) -> None:
        self.FileName = FileName

    def createOrLoadFile(self):
        if self.os.path.exists(self.FileName):
            with open(self.FileName,"r+") as f:
                rlist:list = []
                for line in f:
                    rlist.append(line)
                f.close()
            return rlist
        else:
            file = open(self.FileName,"x")
            file.close()
            return []

    def saveInFile(self,info):
        with open(self.FileName,"a+") as f:
            f.write(info)
            f.close()