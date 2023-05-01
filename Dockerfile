#
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /simple_fastapi/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /simple_fastapi/requirements.txt

#
COPY ./app /simple_fastapi/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]