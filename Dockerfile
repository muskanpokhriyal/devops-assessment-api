FROM python:3.8

COPY requirements.txt ./requirements.txt
COPY app.py ./app.py
COPY client-secret.json ./client-secret.json
COPY sonar.json ./sonar.json

RUN python3 -m venv venv

RUN . venv/bin/activate

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=5050"]