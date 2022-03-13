import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
#from readpro.models import  Task, TaskLog
from readpro.data_objects import Word, Task, TaskLog, Category

def get_object_type(type):
    map_dict = {
        'word' : Word(),
        'task': Task(),
        'task_log': TaskLog(),
        'category': Category(),
    }
    return map_dict.get(type, None)

def do_operation(object,data):
    operation = data['operation']
    data = data['data']
    result = None
    if operation == 'create':
        result = object.create(data)
    elif operation == 'update':
        result = object.update(data)
    elif operation == 'delete':
        result = object.delete(data)
    elif operation == 'get':
        result = object.get_data(data)

    return result
