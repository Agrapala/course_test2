import boto3, json, pymysql, os

sqs = boto3.client('sqs', region_name='ap-south-1')
sns = boto3.client('sns', region_name='ap-south-1')

queue_url = os.getenv('SQS_URL')
topic_arn = os.getenv('SNS_ARN')

while True:
    msgs = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1, WaitTimeSeconds=10)
    if 'Messages' in msgs:
        for msg in msgs['Messages']:
            data = json.loads(msg['Body'])
            conn = pymysql.connect(host=os.getenv('RDS_HOST'), user='admin', password='MyDbPass123', database='courses')
            cur = conn.cursor()
            cur.execute("INSERT INTO registrations (name,email,course_id) VALUES (%s,%s,%s)", 
                        (data['name'], data['email'], data['course_id']))
            conn.commit()
            sns.publish(TopicArn=topic_arn, Message=f"New registration: {data['name']} for course {data['course_id']}")
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])
