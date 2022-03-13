from django.db import models
from django.db import connection
cursor = connection.cursor()
from readpro.helpers.query_helper import create_insert_query, create_update_query, create_delete_query, create_get_query
import logging
logger = logging.getLogger(__name__)
from readpro.app.util.time_helper import convert_timestamp_to_datetime, get_datetime_string

# Create your models here.

class Category(models.Model):
    table_name = 'categories'

    def save(self,details):
        details['created_at'] = get_datetime_string()
        query = create_insert_query(self.table_name, details)
        try:
            cursor.execute(query)
            return True
        except Exception as e:
            logger.exception("Error Creating the data %s" % e)
            return None

    def update(self,task_details,where_fields):
        if 'start_time' in task_details and 'end_time' in task_details:
            task_details['time_spent'] = task_details['end_time']-task_details['start_time']
        if 'start_time' in task_details:
            task_details['start_time'] = convert_timestamp_to_datetime(task_details['start_time'])
        if 'end_time' in task_details:
            task_details['end_time'] = convert_timestamp_to_datetime(task_details['end_time'])

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

    def delete(self,where_fields):
        query = create_delete_query(self.table_name, where_fields)
        try:
            cursor.execute(query)
            return True
        except Exception as e:
            logger.exception("Error Creating the data %s" % e)
            return None

    def get_data(self,where_fields,data):
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
