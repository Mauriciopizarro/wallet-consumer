#
FROM python:3.10

#
WORKDIR /app

#
COPY ./requirements.txt /app/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

#
CMD ["python", "wallet_consumers.py"]