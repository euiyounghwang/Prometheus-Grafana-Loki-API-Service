from fastapi import APIRouter, Request
import json
import datetime
from injector import logger, ESLogPushHandlerInject
from service.status_handler import (StatusHanlder, StatusException)
# from typing import Optional
import datetime
from repository.schema import Log


app = APIRouter(
    prefix="/log",
)


"""
@app.get("/get_alert_log", 
          status_code=StatusHanlder.HTTP_STATUS_200,
          responses={
            200: {"description" : "OK"},
            500 :{"description" : "Unexpected error"}
          },
          description="Sample Payload : GET http://localhost:8010/log/get_alert_log", 
          summary="Get Alert log")
async def get_alert_log(request: Request):
    ''' get json config file from local disk '''
   
    response =  await ESLogHandlerInject.get_service_alert_log()
    if isinstance(response, dict):
        logger.info('get_alert_log: {}]'.format(response))
        
    return response
"""


@app.post("/push_to_loki", 
          status_code=StatusHanlder.HTTP_STATUS_200,
          responses={
            200: {"description" : "OK"},
            500 :{"description" : "Unexpected error"}
          },
          description="Sample Payload : POST http://localhost:8010/log/push_to_loki", 
          summary="Create_log")
async def set_push_loki_log(request_ip:  Request, request_log: Log):
    ''' 
    test curl
    curl -X 'POST'   'http://localhost:8010/log/push_to_loki' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
      "log_status": "error",
      "env": "dev",
      "host": "localhost#1",
      "host_name": "Data_Node_#1",
      "log_filename": "test.log",
      "message": "PROCESS proc"
    }'

    '''
    request_json = request_log.to_json()
    logger.info("request.client.host - : {}, request.json() - {}".format(request_ip.client.host, request_json))
    response =  await ESLogPushHandlerInject.pusho_loki_log(request_ip.client.host, request_json)
    if isinstance(response, dict):
        logger.info('set_push_loki_log [response] - {}'.format(response))

    return response

