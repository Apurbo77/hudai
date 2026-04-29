from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # In a real app, you'd process the form data here (e.g., save to DB or send email)
    return jsonify({"status": "success", "message": "Message received!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
