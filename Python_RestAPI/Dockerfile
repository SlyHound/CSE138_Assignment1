FROM python:3
WORKDIR /application
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m", "flask", "run", "--port=8085", "--host=0.0.0.0" ]