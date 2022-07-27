import os
import sqlite3
from sqlite3 import IntegrityError


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
        try:
            sql = f'''INSERT INTO courses(course_id, course_name, course_timespan, course_fees, course_description) \
            VALUES('{req['course_id']}', '{req['course_name']}', '{req['course_timespan']}', '{req['fees']}', '{req['description']}')'''
            self.conn.execute(sql);
            self.conn.commit()
            self.logger.info("Record created successfully")
            self.conn.close()
        except IntegrityError:
            self.logger.error('Failed to add course into DB as we machine recognised course id as duplicate')
            raise IntegrityError
        except Exception as e:
            self.logger.error('Error Occured while adding record to Courses DB')
            raise Exception

    def insert_multiple_courses(self, courses_req):
        excptns = []
        for course in courses_req:
            try:
                sql = f'''INSERT INTO courses(course_id, course_name, course_timespan, course_fees, course_description) \
                VALUES('{course['course_id']}', '{course['course_name']}', '{course['course_timespan']}', '{course['fees']}', '{course['description']}')'''
                self.conn.execute(sql);
                self.conn.commit()
                self.logger.info("Record created successfully")

            except IntegrityError:
                self.logger.error(f"Failed to add course into DB as we machine recognised course id as duplicate for course_id : {course['course_id']}")
                excptns.append(IntegrityError)
            except Exception as e:
                self.logger.error(f"Error Occured while adding record to Courses DB for course_id : {course['course_id']}")
                excptns.append(Exception)
        self.conn.close()
        return excptns

    def get_all_courses_from_file_system(self):
        try:
            sql = f'''SELECT * FROM courses'''
            self.cursor.execute(sql);
            records = self.cursor.fetchall()
            self.conn.commit()
            self.conn.close()
            return records
        except Exception as e:
            self.logger.error('Error Occured while retrirving  records from Courses DB')
            raise Exception
