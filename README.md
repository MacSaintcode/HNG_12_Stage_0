
# HNG_12_Stage0 Flask API Documentation

## Overview
This is a simple Flask-based API that returns a JSON response containing an email address, the current date and time in ISO 8601 format (UTC), and a GitHub repository URL.

## Requirements
Ensure you have Python installed and the following dependencies:

```sh
pip install flask
```

## Endpoint
### `GET /`

**Description:**
Returns a JSON response with the following data:
- `email`: The email address associated with the API.
- `current_datetime`: The server's current date and time in ISO 8601 format (UTC).
- `github_url`: The GitHub repository URL.

**Example Response:**
```json
{
    "email": "damimakanju@gmail.com",
    "current_datetime": "2025-02-01T14:30:45.123456+00:00",
    "github_url": "https://github.com/MacSaintcode/HNG_12_Stage_0.git"
}
```

## Code Implementation
```python
from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "email": "damimakanju@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/MacSaintcode/HNG_12_Stage_0.git"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
```

## Running the Application
Save the script as `app.py` and run the following command:
```sh
python app.py
```
The server will start and be accessible at `http://127.0.0.1:5000/`.

## Notes
- The `datetime.now(timezone.utc).isoformat()` ensures that the datetime is always returned in ISO 8601 format with UTC timezone.
- Flask should be installed before running the application.

Python: https://hng.tech/hire/python-developers