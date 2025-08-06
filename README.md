FastAPI Book API>>
This is a simple RESTful API built with FastAPI for managing book records. It allows users to fetch,add,update and delete book records using GET,POST,PUT and DELETE requests.

Features>>
- Get book details by ID  
- Add new book details using POST
- Update existing book records using PUT
- Delete a selected book record using DELETE 
- Organized with routers and services for scalability  
- Fully documented with Swagger UI
- 
Project Structure>>
  studyuse/
│
├── main.py # FastAPI app entry point
├── controllers/
│ └── book_controller.py # Route definitions
├── services/
│ └── book_service.py # Business logic
└── README.md
---

Setup Instructions>>
1. Clone the Repository
```bash
git clone https://github.com/sonalsasidharan/studyuse.git

2. Install Dependencies
pip install fastapi uvicorn

3. Run the Application
uvicorn main:app --reload

Now visit: http://127.0.0.1:8000/docs

---
API Endpoints>>

➤ GET /book/{id}
Returns the book details for a given ID.
Example:
GET /book/1
>>this will return the book with id as 1

➤ POST /book/{id}
Adds a new book to the collection.
Request Body:
{
  "title": "The Alchemist",
  "author": "Paulo Coelho"
}

➤ PUT /book/{id}
Updates an existing book.
Request Body:
{
  "title": "Updated Title",
  "author": "Updated Author"
}

➤ DELETE /book/{id}
Deletes a book by its ID.
Example:
DELETE /book/2
---

This project is just for learning and practice. No license.
👤 Author
Lohith Kumar
Siva Kumar
Sonal


---
