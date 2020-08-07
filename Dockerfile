FROM python:3.7.4-slim-stretch

WORKDIR /

# The enviroment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

ADD requirements.txt ./requirements.txt
ADD src/ ./app

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py"]