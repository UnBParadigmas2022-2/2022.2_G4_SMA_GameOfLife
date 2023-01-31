FROM python:3.9

WORKDIR /mesa

COPY . /mesa

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

CMD [ "python3", "-u", "main.py" ]