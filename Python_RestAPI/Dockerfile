FROM python:3
WORKDIR /application
RUN pip3 freeze > requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./Python_RestAPI .
CMD [ "python3", "-m", "flask", "run", "--port=8085", "--host=0.0.0.0" ]