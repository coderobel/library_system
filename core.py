from .utils import track_access
class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return self.title + "by" + self.author
    def __len__(self):
        return self.pages
    def __eq__(self, value):
        if self.title == value.title and self.author == value.author:
            return True
        

class Library():

    def __init__(self,books):
        self.books = books

    def __getitem__(self, index):
        return self.books[index]  

    @track_access
    def borrow_item(self, item, user_id):
        return f"Book '{item.title}' checked out by {user_id}"
    @track_access 
    def return_item(self, item):
        return f"Book '{item}' returned"