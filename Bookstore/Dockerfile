FROM python:3.11-slim

RUN pip install mysql-connector-python
COPY . /app
WORKDIR /app
CMD ["python", "bookstore.py"]
