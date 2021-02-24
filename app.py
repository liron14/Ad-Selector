"""
a file contains the flask app
"""
import json
from typing import Dict, List, Tuple

from flask import Flask, jsonify, request

from algorithms import server_algo

app: Flask = Flask(__name__)

INSERTED_FILES_NUM: int = 0
PROCESSED_FILES_NUM: int = 0


@app.route('/ads', methods=['POST'])
def insert_ads() -> jsonify:
    """
    insert ads
    """
    try:
        global INSERTED_FILES_NUM, PROCESSED_FILES_NUM

        file_names: List[str] = json.loads(request.get_json())

        INSERTED_FILES_NUM = len(file_names)

        server_algo.insert_ads(file_names)

        # enable ad selection
        PROCESSED_FILES_NUM = len(file_names)

        return jsonify('Inserted'), 200

    except Exception as e:
        return jsonify(str(e)), 400


@app.route('/ad_selection', methods=['GET'])
def select_ads() -> jsonify:
    """
    select ads
    """
    try:
        if INSERTED_FILES_NUM == 0 or INSERTED_FILES_NUM != PROCESSED_FILES_NUM:
            raise Exception('server is not ready')

        weights: List[Tuple[str, int]] = json.loads(request.get_json())

        selected_ads: List[Dict[str, int or float]] = server_algo.select_ads(weights)

        return jsonify({'ads': selected_ads}), 200

    except Exception as e:
        return jsonify(str(e)), 400


if __name__ == '__main__':
    app.run()
