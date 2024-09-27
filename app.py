from flask import Flask
import logging

app = Flask(__name__)

# Set up logging to a file
logging.basicConfig(filename='/var/log/myapp/flask.log', level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info("Accessed '/' route")
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
