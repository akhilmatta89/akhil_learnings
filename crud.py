import logging.config

from DataBase.perform_df_opeartions import PerformDBOperations
from helper import Helper


class DBOperations():

    def __init__(self, logger):
        self.logger = logger
        self.perform_db_operations = PerformDBOperations(self.logger)

    def add_course(self, req):
        self.logger.info('Received Request to add Course into Akhil Learnings File System')
        self.perform_db_operations.insert_course(req)
        self.logger.info('Added Course Succesfully')

    def add_courses(self, req) -> list:
        self.logger.info('Received Request to add Courses into Akhil Learnings File System')
        excptns = self.perform_db_operations.insert_multiple_courses(req)
        if not excptns:
            self.logger.info('Added Course Succesfully')
        return excptns

    def retrieve_courses(self) -> list:
        self.logger.info('Received Request to retrive all Courses from Akhil Learnings File System')
        records = self.perform_db_operations.get_all_courses_from_file_system()
        modified_records = Helper().modify_records_view(records)
        if not modified_records:
            self.logger.info('There are no courses present in the Akhil Learnings file system')
            return modified_records
        return modified_records

