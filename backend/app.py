from flask import Flask
from flask_cors import CORS
from routes.phones import phones_bp

app = Flask(__name__)
CORS(app)

# Đăng ký route
app.register_blueprint(phones_bp)

if __name__ == "__main__":
    app.run(debug=True)
