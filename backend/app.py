from flask import Flask, request, jsonify
import redis, boto3, json, os, pymysql

app = Flask(__name__)

redis_client = redis.StrictRedis(host=os.getenv('database-1.cncm40u8c3il.ap-south-1.rds.amazonaws.com'), port=6379, decode_responses=True)
sqs = boto3.client('sqs', region_name='ap-south-1')
queue_url = os.getenv('https://sqs.ap-south-1.amazonaws.com/518335628831/courseReg')

@app.route("/courses", methods=["GET"])
def get_courses():
    cached = redis_client.get("courses")
    if cached:
        return jsonify(json.loads(cached))
    conn = pymysql.connect(host=os.getenv('database-1.cncm40u8c3il.ap-south-1.rds.amazonaws.com'), user='postgress', password='Samitha0130', database='database-1')
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, image_url FROM courses")
    data = [{"id": i[0], "title": i[1], "description": i[2], "image": i[3]} for i in cur.fetchall()]
    redis_client.set("courses", json.dumps(data))
    return jsonify(data)

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data.get("name") or not data.get("email") or not data.get("course_id"):
        return jsonify({"error": "Missing fields"}), 400
    sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(data))
    return jsonify({"status": "Registration submitted"})
