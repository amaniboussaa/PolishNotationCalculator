# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory
WORKDIR /app


# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY ./api ./api
COPY ./tests ./tests

# Command to run the application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]



