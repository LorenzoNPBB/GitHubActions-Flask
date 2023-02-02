FROM python:3.9.16-alpine3.16

WORKDIR /appFlask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#Esto es para arrancarlo para produccion
RUN pip3 install gunicorn 

COPY . .

EXPOSE 4000

WORKDIR /appFlask/FlaskApp
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

#ENTRYPOINT [ "python3", "/appFlask/entry_point.py"]
CMD ["./entrypoint.sh"]

