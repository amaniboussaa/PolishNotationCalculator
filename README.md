# Reverse Polish Notation (RPN) Calculator API
## Setup Instructions

Follow the steps below to set up the project locally:

### 1. Create a Virtual Environment

First, create a virtual environment for the project:

```bash
python -m venv venv
```
### 2.Activate the Virtual Environment
```bash
source venv/Scripts/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt

```
### 4. Run the Application
```bash
uvicorn api.main:app --reload
```
## Interactive API docs¶
Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided by Swagger UI):

## Test
```bash
pytest
```