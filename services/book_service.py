book_data={1:{"title":"haryy potter","author":"JK rowling"},2:{"title":"lord of the rings","author":"john donald"}}
def get_id(book_id:  int):
    return book_data.get(book_id,{'error':'book not found'})
def add_book(book_id:int,book:dict):
    if book_id in book_data:
        return None
    book_data[book_id]=book
    return book_data[book_id]
def update_book(book_id:int,book:dict):
    if book_id not in book_data:
        return None
    book_data[book_id]=book
def delete_book(book_id:int):
    return book_data.pop(book_id,None)
