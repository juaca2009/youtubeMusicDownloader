FROM python:3

RUN apt update  

WORKDIR /usr/src/app

RUN apt install ffmpeg -y

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]
