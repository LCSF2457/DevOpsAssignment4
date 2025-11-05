from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# display msg from env variable APP_MESSAGE on home route(/)
@app.route("/")
def home():
    return f"<p>{os.getenv('APP_MESSAGE')}</p>"

# display 2nd env variable APP_HEALTH on health route(/health)
@app.route("/health")
def health():
    return f"<p>{os.getenv('APP_HEALTH')}</p>"
