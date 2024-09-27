import logging
from flask import Flask

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    filename='/var/log/myapp/flask.log', 
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

@app.route('/')
def index():
    app.logger.info('Home page accessed')
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
