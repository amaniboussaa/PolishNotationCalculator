from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from api.models import Base, Operation

from api.database import engine,get_db
from sqlalchemy.orm import Session
import csv
from fastapi.middleware.cors import CORSMiddleware

# Initialize DB
Base.metadata.create_all(bind = engine)
from io import StringIO
from fastapi.responses import StreamingResponse

# Initialize FastAPI
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change this to specific domains for production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

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
    
# Define a Pydantic model for the request body
class ExpressionRequest(BaseModel):
    expression: str  # This will define the expected structure of the request body


@app.post("/calculate/",status_code=status.HTTP_201_CREATED)
async def calculate(request: ExpressionRequest, db: db_dependency):
    expression = request.expression
    result = evaluate_rpn(expression)
    operation = Operation(expression=expression, result=result)
    db.add(operation)
    db.commit()
    return {"expression": expression, "result": result}


# Route to download CSV
@app.get("/export/", status_code=status.HTTP_200_OK)
async def export_data(db: Session = Depends(get_db)):
    operations = db.query(Operation).all()
    
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Expression", "Result"])
    for operation in operations:
        writer.writerow([operation.id, operation.expression, operation.result])
    
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=operations.csv"})