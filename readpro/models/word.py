from django.db import models
from django.contrib.auth.models import User

from readpro.models.category import Category
from django.db import connection
cursor = connection.cursor()
from readpro.helpers.query_helper import create_insert_query, create_update_query, create_delete_query, create_get_query
import logging
logger = logging.getLogger(__name__)

# Create your models here.

class Word(models.Model):
    table_name = 'word'
    
    def save_word(self,word_details):
        query = create_insert_query(self.table_name, word_details)
        print(query)
        try:
            cursor.execute(query)
            return True
        except Exception as e:
            logger.exception("Error Creating the data %s" % e)
            return None
        
    def update_word(self,word_details,where_fields):
        query = create_update_query(self.table_name, word_details, where_fields)
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
        
    def delete_word(self,where_fields):
        query = create_delete_query(self.table_name, where_fields)
        try:
            cursor.execute(query)
            return True
        except Exception as e:
            logger.exception("Error Creating the data %s" % e)
            return None
        
    def get_word_data(self,where_fields):
        query = create_get_query(self.table_name, where_fields)
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
    
    def get_word(self,id=None):
        query = "SELECT * from word"
        where_clause = ""
        if id:
            where_clause = " where id = %s" % id
        complete_query = query+where_clause+';'
        try:
            cursor.execute(complete_query)
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        except Exception:
            return None