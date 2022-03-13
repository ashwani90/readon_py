OPERATION_MAPPING_FAILED = {
    "get": "fetch",
    "create": "create",
    "delete": "delete",
    "update": "update"
}

OPERATION_MAPPING_SUCCESS = {
    "get": "fetched",
    "create": "created",
    "delete": "deleted",
    "update": "updated"
}

MODEL_MAPPING = {
    "task": "task",
    "task_log": "task log",
    "word": "word",
    "category": "category",
}

def getSuccessMessage(data=None, object_type=False,operation=False):
    response_data = {}
    response_data['status'] = True
    if not object_type or not operation:
        response_data['message'] = "Success"
    else:
        response_data['message'] = "Successfully %s %s data" % (OPERATION_MAPPING_SUCCESS[operation],MODEL_MAPPING[object_type])
    if data:
        response_data['data'] = data
    else:
        response_data['data'] = []
    return response_data

def getErrorMessage(object_type=False,operation=False):
    response_data = {}
    response_data['status'] = False
    if not object_type or  not operation:
        response_data['message'] = "Failed data entity"
    else:
        response_data['message'] = "Failed to %s %s data" % (OPERATION_MAPPING_FAILED[operation],MODEL_MAPPING[object_type])
    return response_data
