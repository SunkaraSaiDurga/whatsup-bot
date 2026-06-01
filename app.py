from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 My WhatsApp AI Bot</h1>
    <p>Server is running successfully.</p>
    """

@app.route("/about")
def about():
    return "This bot is built using Python and Flask."

if __name__ == "__main__":
    app.run(debug=True)