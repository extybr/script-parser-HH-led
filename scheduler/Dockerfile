FROM python:alpine

WORKDIR /scheduler

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]