FROM python:3.14-slim

# set work dir
WORKDIR /app

# install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of app into container
COPY . .

# open port 5000 (what flask seems to use)
EXPOSE 5000

# flask env variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# run app
CMD ["flask", "run"]
