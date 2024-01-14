FROM python:3.9-slim

WORKDIR /word-count

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "word-count.py"]