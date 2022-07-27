import logging.config

from DataBase.perform_df_opeartions import PerformDBOperations


class DBOperations():

    def __init__(self, logger):
        self.logger = logger

    def add_course(self, req):
        self.logger.info('Received Request to add Courses into Akhil Learnings File System')
        perform_db_operations = PerformDBOperations(self.logger)
        perform_db_operations.insert_course(req)
        self.logger.info('Added Courses Succesfully')
