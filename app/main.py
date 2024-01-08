from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from connect import SessionLocal
from models import Todo as TodoModel
from pydantic import BaseModel

# Pydantic model
class Todo(BaseModel):
    task: str
    completed: bool

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos/")
def create_todo(todo: Todo, db: Session = Depends(get_db)):
    todo_model = TodoModel(**todo.dict())  # Convert Pydantic model to SQLAlchemy model
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo, db: Session = Depends(get_db)):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updated_todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}
