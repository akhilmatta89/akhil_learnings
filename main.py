import json

from flask import Flask, request, jsonify  # return flask.response object
import sqlite3
from sqlite3 import Error, IntegrityError
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


@app.route('/add_course', methods=['POST'])
def add_course():
    """ This Method is used to add a single course to File system"""
    req = request.json
    try:
        # ToDo Need to add validation to make sure all the inputs are given by user
        DBOperations(logger).add_course(req)
        return json.dumps({'Status':'Course added succesfully','Status_code':200})
    except IntegrityError:
        return json.dumps({'Status': f'machine recognised course id as duplicate',
                           'status_code': 409})
    except Exception as e:
        return json.dumps({'Status': f'Error while inserting the Record with exception {e}',
                           'status_code': 500})

@app.route('/add_courses', methods=['POST'])
def add_courses():
    """ This Method is used to add a multiple course to File system"""
    # ToDo Need to add validation to make sure all the inputs are given by user
    req = request.json
    try:
        any_exceptions = DBOperations(logger).add_courses(req)
        if not any_exceptions:
            return json.dumps({'Status':'Courses added succesfully','Status_code':200})
        if any_exceptions:
            raise any_exceptions[0]
    except IntegrityError:
        return json.dumps({'Status': f'machine recognised course id as duplicate refer logs for course_id',
                           'status_code': 409})
    except Exception as e:
        return json.dumps({'Status': f'Error while inserting the Records with exception {e}, refer logs for course_id',
                           'status_code': 500})

@app.route('/retrieve_courses', methods=['GET'])
def retrieve_courses():
    """ This Method is used to retrive all records from file system"""
    # ToDo Need to add validation to make sure all the inputs are given by user
    try:
        records = DBOperations(logger).retrieve_courses()
        return json.dumps(records)
    except Exception as e:
        return json.dumps({'Status': f'Error while inserting the Records with exception {e}, refer logs for course_id',
                           'status_code': 500})


if __name__ == "__main__":
    print('******************* Welcome to Akhil Learnings **************************')
    if 'Akhillearnings.db' not in current_directory:
        create_connection()
        PerformDBOperations(logger).add_courses_table()
    app.run(debug=True)
