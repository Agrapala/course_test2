FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask redis boto3 pymysql
CMD ["python3.10", "app.py"]
