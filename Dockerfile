FROM python:3.11-slim
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY . /opt/app
WORKDIR /opt/app/mysite
CMD ["python", "manage.py", "runserver", "0:8000"]
