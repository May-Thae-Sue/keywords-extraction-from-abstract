# FROM python:3.7-alpine
# WORKDIR /app
# RUN pip install nltk
# COPY example.py .

# For flask
FROM python:3.7-alpine
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m nltk.downloader all -d .
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY . .
CMD ["python", "app.py"]
