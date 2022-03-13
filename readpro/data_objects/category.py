from readpro.models import Category as Model
import logging
from .base import Base
# Get an instance of a logger
logger = logging.getLogger(__name__)

class Category(Base):
    all_fields = ["name","description"]
    optional_fields = ["parent_ids","child_ids","created_at", "id"]
    def create(self, data):
        fields = Base.create_fields(self,data)
        if not fields:
            return None
        model = Model()
        data = model.save(fields)
        return data

    def update(self,data):
        fields = Base.check_update_fields(self,data)
        where_fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None
        model = Model()
        data = model.update(fields, where_fields)
        return data

    def delete(self,data):
        fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None
        model = Model()
        data = task.delete(fields)
        return data

    def get_data(self,data):
        fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            fields = {}
        model = Model()
        data = model.get_data(fields,data)
        return data
