from flask import Flask,jsonify
from datetime import datetime,timezone
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.get("/")
def home():
    return jsonify(
        {"email": "damimakanju@gmail.com",
         "current_datetime": datetime.utcnow().replace(microsecond=0).isoformat() + 'Z',
         "github_url": "https://github.com/MacSaintcode/HNG_12_Stage_0"}),200


if __name__ == "__main__":
    app.run(debug=True)
