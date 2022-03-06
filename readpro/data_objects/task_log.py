from readpro.models import TaskLog as TaskModel
import logging
from .base import Base
# Get an instance of a logger
logger = logging.getLogger(__name__)

class TaskLog(Base):
    all_fields = ["description"]
    optional_fields = ["time_spent","start_time","end_time", "created_at", "id"]
    def create(self, data):
        fields = Base.create_fields(self,data)
        if not fields:
            return None
        task = TaskModel()
        data = task.save_task_log(fields)
        return data

    def update(self,data):
        fields = Base.check_update_fields(self,data)
        where_fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None
        task = TaskModel()
        data = task.update_task_log(fields, where_fields)
        return data

    def delete(self,data):
        fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            return None
        task = TaskModel()
        data = task.delete_task_log(fields)
        return data

    def get_data(self,data):
        fields = Base.check_where_clause(self,data['where_clause'])
        if not fields:
            fields = {}
        task = TaskModel()
        data = task.get_task_log_data(fields,data)
        return data
