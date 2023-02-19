FROM python:3.9-slim-buster
RUN pip3 install uvicorn
COPY ./src /app/Assignment
COPY ./requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "Assignment.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]