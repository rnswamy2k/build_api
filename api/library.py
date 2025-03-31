from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "title one", "author": "author one", "category": "math"},
    {"title": "title two", "author": "author two", "category": "engineering"},
    {"title": "title three", "author": "author three", "category": "math"},
    {"title": "title four", "author": "author four", "category": "history"},
    {"title": "title five", "author": "author five", "category": "engineering"},
    {"title": "title six", "author": "author six", "category": "math"},
    ]   


@app.get("/books")
async def get_all_book():
    return BOOKS

@app.get("/books/{book_title}")
async def get_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {"error": "Book not found"}

@app.get("/books/")
async def get_book_by_category(category: str):
    books = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books.append(book)
    return books

@app.get("/books/{author_name}/")
async def get_book_by_category_and_author(author_name: str, category: str):
    books = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold() and \
            book.get("category").casefold() == category.casefold():
            books.append(book)
    return books

@app.get("/books/get/{author_name}")
async def get_book_by_author(author_name: str):
    books = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold():
            books.append(book)
    return books


@app.post("/books/create_book")
async def create_book(book=Body()):
    BOOKS.append(book)
    return {"message": "Book created successfully", "book": book}

@app.put("/books/update_book")
async def update_book(book=Body()):
    for index, b in enumerate(BOOKS):
        if b.get("title").casefold() == book.get("title").casefold():
            BOOKS[index] = book
            return {"message": "Book updated successfully", "book": book}
    return {"error": "Book not found"}

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for index, b in enumerate(BOOKS):
        if b.get("title").casefold() == book_title.casefold():
            BOOKS.pop(index)
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}