import uuid

class Book:
    def __init__(self, **kwargs):
        # you have to use [''] style to read a dict
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.serial_id = kwargs['serial_id']

class LibraryBook(Book):
    def __init__(self, **kwargs):
        # where I made mistake
        super().__init__(**kwargs)
        self.id = str(uuid.uuid4())

class Member:
    def __init__(self, name: str, id: str):
        self.name = name
        self.social_id = id

class LibraryMember(Member):
    def __init__(self, member: Member):
        # Map member attributes to Member constructor parameters
        super().__init__(name=member.name, id=member.social_id)
        self.id = str(uuid.uuid4())

class Library:
    def __init__(self, name: str):
        self.name = name
        self.members = []
        self.books_dict = {}
        self.lendings_dict = {}

    def register_member(self, member: Member) -> LibraryMember:
        lm = self.__find_member(member)
        
        if not lm:
            lm = LibraryMember(member)
            self.members.append(lm)

        return lm
        

    def buy_book(self, book: Book):
        newBook = LibraryBook(name=book.name, description=book.description, serial_id=book.serial_id)

        if book.serial_id in self.books_dict:
            # python uses append, not push
            self.books_dict[book.serial_id].append(newBook)
        else:
            self.books_dict[book.serial_id] = [newBook]
    
    def lend_book(self, book: LibraryBook, member: Member):
        lm = self.__find_member(member)
        
        if not lm:
          lm = self.register_member(member)
        
        if lm.id in self.lendings_dict:
            self.lendings_dict[lm.id].append(book)
        else:
            self.lendings_dict[lm.id] = [book]
            
        self.books_dict[book.serial_id].remove(book)

        
    def __find_member(self, member: Member):
        for lm in self.members:
            if lm.social_id == member.social_id:
                return lm
        return None
