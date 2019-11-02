# FROM python:3.7-alpine
# WORKDIR /app
# RUN pip install nltk
# COPY example.py .

# For flask
FROM python:3.7-alpine
WORKDIR /
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m nltk.downloader -d ./nltk_data all
RUN apk update && apk add bash
COPY . .
ENV FLASK_APP /app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_DEBUG=1
ENV FLASK_DEVELOPMENT=1
CMD ["flask", "run"]
