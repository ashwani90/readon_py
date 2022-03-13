def getSuccessResponse(data=None):
    response_data = {}
    response_data['status'] = True
    response_data['message'] = "Successfully Created Object"
    if data:
        response_data['data'] = data
    else:
        response_data['data'] = []
    return response_data

def getFailedResponse():
    response_data = {}
    response_data['status'] = False
    response_data['message'] = "Failed Object fetch"
