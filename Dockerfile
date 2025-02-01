# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to avoid Python writing .pyc files and ensure the output is sent straight to the terminal
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose port 8000 (Django default port)
EXPOSE 8000

# Run Django's development server (use `python manage.py runserver 0.0.0.0:8000` to allow access from outside the container)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

