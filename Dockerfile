FROM python:3.8

WORKDIR /

COPY packages.txt .
COPY collect.py .

RUN pip install -r ./packages.txt

ENTRYPOINT [ "python3","-u", "collect.py" ] 

