FROM python:3
MAINTAINER Michele Rastelli
LABEL description="Sample application for docker seminar."

RUN pip install pytime
ADD ./easterCalculator /app
WORKDIR /app
CMD python /app/main.py
