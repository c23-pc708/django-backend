FROM python:3.10-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONUNBUFFERED=1

EXPOSE 8080

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]