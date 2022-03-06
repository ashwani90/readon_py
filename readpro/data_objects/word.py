from readpro.models import Word as WordModel
import logging
from .base import Base
# Get an instance of a logger
logger = logging.getLogger(__name__)

class Word(Base):
    all_fields = ["name","meaning"]
    optional_fields = ["id", "created_at","updated_at"]
    def create(self, data):
        fields = Base.create_fields(self,data)
        if not fields:
            return None
        word = WordModel()
        data = word.save_word(fields)
        return data
    
    def update(self,data):
        fields = Base.check_update_fields(self,data)
        where_fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None
        word = WordModel()
        data = word.update_word(fields, where_fields)
        return data 
    
    def delete(self,data):
        fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None 
        word = WordModel()
        data = word.delete_word(fields)
        return data 
    
    def get_data(self,data):
        fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None 
        word = WordModel()
        data = word.get_word_data(fields)
        return data