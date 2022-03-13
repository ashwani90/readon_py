from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import JsonResponse
from readpro.models import Word
import json
from readpro.helpers.api_helper import getSuccessMessage,getErrorMessage
from readpro.helpers.object_helpers import get_object_type, do_operation
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        response_data = {}
        response_data['content'] = "abcv"

        return JsonResponse(response_data)

@csrf_exempt
def save_word(request):
    if request.method == 'POST':
        word = Word()
        word_details = json.loads(request.body)
        if word.save_word(word_details):
            return JsonResponse(getSuccessMessage())
        else:
            return JsonResponse(getErrorMessage())

@csrf_exempt
def get_word(request):
    word = Word()
    data = json.loads(request.body)
    id = data['id']
    try:
        word_data = word.get_word(id)
        return JsonResponse(getSuccessMessage(word_data))
    except Exception as e:
        logger.exception(e)
        return JsonResponse(getErrorMessage())

@csrf_exempt
def create_object(request):
    data=False
    try:
        data = json.loads(request.body)
    except Exception as e:
        logger.exception(e)
    if not data:
        data = request.GET.dict()
        data['data'] = json.loads(data['data'])
        logger.info(data)
    object = get_object_type(data['object_type'])
    result = do_operation(object,data)

    if result == None or result == False:
        return JsonResponse(getErrorMessage(data['object_type'],data['operation']))
    else:
        return JsonResponse(getSuccessMessage(result,data['object_type'],data['operation']))
