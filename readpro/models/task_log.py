from django.db import models
from django.db import connection
cursor = connection.cursor()
from readpro.helpers.query_helper import create_insert_query, create_update_query, create_delete_query, create_get_query
import logging
logger = logging.getLogger(__name__)

# Create your models here.

class TaskLog(models.Model):
    table_name = 'task_logs'

    def save_task_log(self,task_details):
        query = create_insert_query(self.table_name, task_details)
        print(query)
        try:
            cursor.execute(query)
            return True
        except Exception as e:
            logger.exception("Error Creating the data %s" % e)
            return None

    def update_task_log(self,task_details,where_fields):
        query = create_update_query(self.table_name, task_details, where_fields)
        try:
            cursor.execute(query)
            query = create_get_query(self.table_name, where_fields)
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        except Exception as e:
            logger.exception("Error Creating the data %s" % e)
            return None

    def delete_task_log(self,where_fields):
        query = create_delete_query(self.table_name, where_fields)
        try:
            cursor.execute(query)
            return True
        except Exception as e:
            logger.exception("Error Creating the data %s" % e)
            return None

    def get_task_log_data(self,where_fields,data):
        query = create_get_query(self.table_name, where_fields,data)
        try:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        except Exception as e:
            logger.exception("Error fetching the data %s" % e)
            return None
