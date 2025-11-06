from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# display msg from env variable APP_MESSAGE on home route(/)
@app.route("/")
def home():
    return render_template('index.html', message=os.getenv('APP_MESSAGE'))

# display 2nd env variable APP_HEALTH on health route(/health)
@app.route("/health")
def health():
    return render_template('health.html', message=os.getenv('APP_HEALTH'))
