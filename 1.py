# импортируем библиотеки
from flask import Flask, request, jsonify
# import logging
import json

app = Flask(__name__)

# Устанавливаем уровень логирования
# logging.basicConfig(level=logging.INFO)

@app.route('/')
def main():
    data = json.load(open('data.json'))
    return jsonify(data)


if __name__ == '__main__':
    app.run()