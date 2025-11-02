FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install boto3 pymysql
CMD ["python3.10", "worker.py"]
