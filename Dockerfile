FROM python:3.10
#
WORKDIR /simple_fastapi

#
COPY ./requirements.txt /simple_fastapi/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /simple_fastapi/requirements.txt

#
COPY ./simple_fastapi /simple_fastapi

#
CMD ["uvicorn", "simple_fastapi.main:app", "--host", "0.0.0.0", "--port", "80"]