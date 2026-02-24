from flask import Flask, render_template, request, jsonify
from data import college_info
import os

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")

# Home route
@app.route("/", methods=["GET", "HEAD"])
def home():
    return render_template("index.html")

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Loop through college_info
    for keys, response in college_info.items():
        # Handle tuple keys
        if isinstance(keys, tuple):
            for word in keys:
                if word.lower() in user_message:
                    return jsonify({"reply": response})
        # Handle string keys
        elif isinstance(keys, str):
            if keys.lower() in user_message:
                return jsonify({"reply": response})

    # Default response if no match
    return jsonify({"reply": "Sorry, I don't understand your question."})

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

