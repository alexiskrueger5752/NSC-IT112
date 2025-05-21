FROM python:3.12-slim
COPY ./requirements.txt /requirements.txt
COPY ./django_app .
RUN pip install -r requirements.txt
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]