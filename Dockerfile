FROM python:3.13.5-bullseye

EXPOSE 80

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .


ENTRYPOINT ["python", "app.py"]