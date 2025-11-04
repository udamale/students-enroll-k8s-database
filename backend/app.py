from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend

# RDS MySQL config
db_config = {
    "host": "database-2.c9266mewer2a.eu-west-1.rds.amazonaws.com",
    "user": "admin",
    "password": "Cloud1234",
    "database": "abi"
}

def get_db_connection():
    return pymysql.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"]
    )

@app.route("/api/save", methods=["POST"])
def save_user():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cursor.execute(sql, (email, password))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
