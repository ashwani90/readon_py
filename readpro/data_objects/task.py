from readpro.models import Task as TaskModel
import logging
from .base import Base
# Get an instance of a logger
logger = logging.getLogger(__name__)

class Task(Base):
    all_fields = ["name"]
    optional_fields = ["id", "due_date","time_spent","created_at", "parent_task", "completed_date", "start_date"]
    def create(self, data):
        fields = Base.create_fields(self,data)
        if not fields:
            return None
        task = TaskModel()
        data = task.save_task(fields)
        return data

    def update(self,data):
        fields = Base.check_update_fields(self,data)
        where_fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None
        task = TaskModel()
        data = task.update_task(fields, where_fields)
        return data

    def delete(self,data):
        fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None
        task = TaskModel()
        data = task.delete_task(fields)
        return data

    def get_data(self,data):
        fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            fields = {}
        task = TaskModel()
        data = task.get_task_data(fields,data)
        return data
