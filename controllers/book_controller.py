from fastapi import APIRouter
from models.book_models import Book
from services.book_service import get_id,add_book,update_book,delete_book
router=APIRouter()
@router.get("/book/{id}")
def get_book(id:int):
    return get_id(id)

@router.post("/book/{id}")
def create_book(id:int,book:Book ):
    result=add_book(id,book.dict())
    if result is None:
        return {"error":"book already exists"}
    return {"message":"book added","data":result}

@router.put("/book/{id}")
def up_book(id:int,book:Book):
    result=update_book(id,book.dict())
    if result is None:
        return {"error":"book not found"}
    return {"message":"book details updated","data":result}

@router.delete("/book/{id}")
def del_book(id:int):
    result=delete_book(id)
    if result is None:
        return {"error":"book does not exist"}
    return {"message":"book details deleted","data":result}
