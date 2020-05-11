FROM python:3

WORKDIR /home/james/learning/syllaboard

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY  . .

CMD ["flask", "run"]