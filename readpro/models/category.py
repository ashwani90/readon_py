from django.db import models
from django.db import connection
cursor = connection.cursor()
from readpro.helpers.query_helper import create_insert_query, create_update_query, create_delete_query, create_get_query
import logging
logger = logging.getLogger(__name__)
from readpro.app.util.time_helper import convert_timestamp_to_datetime, get_datetime_string
import json
# Create your models here.

class Category(models.Model):
    table_name = 'categories'
    field_types = {
        "parent_ids": "array",
        "child_ids": "array"
    }

    def save(self,details):
        details['created_at'] = get_datetime_string()
        details['parent_ids'] = parse_python_array_to_postgres(details['parent_ids'])
        details['child_ids'] = parse_python_array_to_postgres(details['child_ids'])
        query = create_insert_query(self.table_name, details)
        try:
            cursor.execute(query)
            return True
        except Exception as e:
            logger.exception("Error Creating the data %s" % e)
            return None

    def update(self,details,where_fields):
        if 'parent_ids' in details:
            details['parent_ids'] = parse_python_array_to_postgres(details['parent_ids'])
        if 'child_ids' in details:
            details['child_ids'] = parse_python_array_to_postgres(details['child_ids'])

        query = create_update_query(self.table_name, details, where_fields)

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

def parse_python_array_to_postgres(array):
    joined_string = "{" + ",".join(str(v) for v in array) + "}"
    return joined_string
