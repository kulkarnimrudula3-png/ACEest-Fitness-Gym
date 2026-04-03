FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask pytest

CMD ["python", "app.py"]