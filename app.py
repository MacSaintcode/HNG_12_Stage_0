from flask import Flask,jsonify
from datetime import datetime,timezone
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.get("/")
def home():
    return jsonify(
        {"email": "damimakanju@gmail.com",
         "current_datetime": datetime.now(timezone.utc).isoformat(),
         "github_url": "https://github.com/MacSaintcode/HNG_12_Stage_0.git"}),200


if __name__ == "__main__":
    app.run(debug=True)
