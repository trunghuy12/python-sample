FROM python:3.9-slim-buster

RUN adduser muser
WORKDIR /home/muser

COPY Pipfile* ./
RUN pip3 install pipenv
RUN pipenv install --system

COPY project project 
COPY migrations migrations
COPY instance instance
COPY app.py config.py boot.sh ./

ENV FLASK_APP app.py

RUN chown -R muser:muser ./ && chmod +x boot.sh
USER muser

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
