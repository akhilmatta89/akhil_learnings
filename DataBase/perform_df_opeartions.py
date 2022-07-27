import os
import sqlite3


class PerformDBOperations():

    def __init__(self, logger):
        # Connecting to sqlite
        conn = sqlite3.connect('Akhillearnings.db')
        # Creating a cursor object using the cursor() method
        self.cursor = conn.cursor()
        self.conn = conn
        self.logger = logger

    def add_courses_table(self):
        # Creating table as per requirement
        dir_path = os.path.dirname(os.path.abspath(__file__))
        with open(dir_path + '/courses_table.sql', 'r') as sql_file:
            sql_script = sql_file.read()

        db = sqlite3.connect('Akhillearnings.db')
        cursor = db.cursor()
        cursor.executescript(sql_script)
        db.commit()
        db.close()
        self.logger.info("Table created successfully")

    def retrieve_all_courses(self):
        sql = '''SELECT * FROM courses'''
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def insert_course(self, req):
        course_id = req['course_id']
        course_name = req['course_name']
        course_timespan = req['course_timespan']
        course_fees = req['fees']
        course_description = req['description']
        try:
            sql = f'''INSERT INTO courses(course_id, course_name, course_timespan, course_fees, course_description) \
            VALUES('{course_id}', '{course_name}', '{course_timespan}', '{course_fees}', '{course_description}')'''
            self.conn.execute(sql);
            self.conn.commit()
            self.logger.info("Record created successfully")
            self.conn.close()
        except Exception as e:
            self.logger.error('Error Occured while adding record to Courses DB')
            raise Exception