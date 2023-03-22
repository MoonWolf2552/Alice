from flask import Flask, request
import logging
import json
from app_funk import cloud_func

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s %(levelname)s %(name)s %(message)s')

@app.route('/post', methods=['POST'])
def main():

    logging.info('Request: %r', request.json)

    response = cloud_func(request.json, '')

    logging.info('Request: %r', response)

    return json.dumps(response)


if __name__ == '__main__':
    app.run()
