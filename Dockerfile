FROM python:3.10.11

COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "zktest.py" ]