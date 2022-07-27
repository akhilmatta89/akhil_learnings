import json

from flask import Flask, request, jsonify  # return flask.response object
import sqlite3
from sqlite3 import Error
import os

from DataBase.perform_df_opeartions import PerformDBOperations
from crud import DBOperations
import logging
import logging.config

current_directory = os.path.dirname(os.path.abspath(__file__))

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome To The Course API"


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect('Akhillearnings.db')
        logger.info(f'The sqlite version using in the project is {sqlite3.version}')
    except Error as e:
        logger.error(f'There is the an error while creating DataBase and the error is {e}')
    finally:
        if conn:
            conn.close()


@app.route('/courses-provided', methods=['POST'])
def add_courses():
    req = request.json
    try:
        """ This Method is used to add a single course to File system"""
        DBOperations(logger).add_course(req)
        return json.dumps({'Status':'Course added succesfully','Status_code':200})
    except Exception as e:
        return json.dumps({'Status': f'Error while inserting the Record with exception {e}',
                           'status_code': 500})


if __name__ == "__main__":
    if 'Akhillearnings.db' not in current_directory:
        create_connection()
        PerformDBOperations(logger).add_courses_table()
    app.run(debug=True)
