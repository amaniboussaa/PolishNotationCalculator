from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from api.models import Base, Operation

from api.database import engine,get_db
from sqlalchemy.orm import Session

# Initialize DB
Base.metadata.create_all(bind = engine)

# Initialize FastAPI
app = FastAPI()

db_dependency = Annotated[Session,Depends(get_db)]

# Function to evaluate Reverse Polish Notation (RPN)
def evaluate_rpn(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/calculate/",status_code=status.HTTP_201_CREATED)
async def calculate(expression: str, db: db_dependency):
    result = evaluate_rpn(expression)
    operation = Operation(expression=expression, result=result)
    db.add(operation)
    db.commit()
    return {"expression": expression, "result": result}
