from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import logging

app = Flask(__name__)
metrics = PrometheusMetrics(app)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

@app.route('/')
def hello():
    logger.info('Hello endpoint accessed')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
