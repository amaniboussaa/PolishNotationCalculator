# Reverse Polish Notation (RPN) Calculator API
## Description

A brief description of your project, its purpose, and what it does.

## Technologies Used

- Python 3.11
- FastAPI
- MySQL
- Docker
- Docker Compose
### Prerequisites
- Docker
- Docker Compose
## Setup Instructions

### 1. Create the `.env` File

In the root directory of your project, create a file named `.env` and add the following content:

```bash
# MySQL Root Password
MYSQL_ROOT_PASSWORD=my-secure-root-password  # A strong password for the root user.

# MySQL Database Name
MYSQL_DATABASE=my_database_name  # The name of the database your application will use.

# MySQL User
MYSQL_USER=my_app_user  # A username for your application to connect to the database.

# MySQL User Password
MYSQL_PASSWORD=my-secure-password  # A strong password for the application user.

```
Make sure to customize the values as needed.

### 2.Build and Run the Application
```bash
docker-compose up --build
```
## Interactive API docs
Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided by Swagger UI):

### 4. Stopping the Application
```bash
docker-compose down
```


### 5. Running tests
```bash
docker-compose run backend pytest tests
```