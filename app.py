import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Register blueprints
from routes.random_word import bp as random_word_bp
app.register_blueprint(random_word_bp)


@app.route("/")
def index():
    return jsonify({"message": "Devin Curtis - Portfolio Backend API", "status": "running"})


# This only runs when you execute: python app.py
if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    app.run(debug=debug, port=port)
