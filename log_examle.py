import logging

import requests

logging.basicConfig(level=logging.DEBUG,
                    filename='example.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s'
                    )


def test_request(url='https://yandex.ru'):
    result = requests.get(url)
    # logging.debug(result.status_code)
    # logging.info(result.text)
    if not result:
        logging.error(f'url {url} return code: {result.status_code}')


def log():
    i = 0
    while i < 10:
        logging.warning(i)
        i += 1


if __name__ == '__main__':
    test_request()
