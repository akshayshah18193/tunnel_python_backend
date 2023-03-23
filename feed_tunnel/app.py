# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
__author__ = 'Akshay'

from flask_cors import CORS
from flask import Flask, render_template, request, json
from backend.tunnel_service import TunnelService
from backend.entity.entity import HashDataSchema

app = Flask(__name__)
CORS(app)


@app.route('/hashgrab/<string:q>', methods=['GET'])
def hashgrab(q):
    args = request.args.get('q')

    hashtag_name = q
    print(hashtag_name)
    response = TunnelService.getHashData(hashtag_name)
    print(response)
    return json_response(response, 200)


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})


if __name__ == '__main__':
    # TunnelService.getHashData('bosch')
    app.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
