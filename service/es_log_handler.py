
import requests
from service.status_handler import StatusException
import json
import os
import socket
import logging
import logging_loki
from dotenv import load_dotenv

load_dotenv()

class ESLogPushHandler(object):
    
    def __init__(self, logger):
        self.logger = logger

        """ ---------------- """
        """ Grafana Loki """
        logging_loki.emitter.LokiEmitter.level_tag = "level"
        # assign to a variable named handler 
        handler = logging_loki.LokiHandler(
        url="http://{}:3100/loki/api/v1/push".format(os.getenv("LOKI_HOST")),
        version="1",
        )
        # create a new logger instance, name it whatever you want
        self.loki_logger = logging.getLogger("loki-api-logger")
        self.loki_logger.addHandler(handler)
        """ ---------------- """
        
      
    async def pusho_loki_log(self, client_ip, request_json):
        ''' Update log to H2 database'''
        try:
            self.logger.info(f"client_ip : {client_ip}, request_json : {request_json}")
            message = request_json.get("message")
            Logging_Header = "Prometheus-Logging-Service - [{}] Spark Node [{}] {} - Spark Custom App ['{}'] Log : {}".format(request_json.get("env"), request_json.get("host"), request_json.get("log_status"), request_json.get("log_filename"), message)
            if request_json.get("log_status").upper() == "INFO":
                self.loki_logger.info(Logging_Header,
                                        extra={"tags": {"service": "prometheus-grafana-loki-logging-service", "message" : "[{}] Services, Alert : {}".format(
                                            request_json.get("env"),
                                            request_json.get("log_status")
                                            ), 
                                            "env" : "{}".format(request_json.get("env")), 
                                            }},
                )
            elif request_json.get("log_status").upper() == "ERROR":
                self.loki_logger.error(Logging_Header,
                                        extra={"tags": {"service": "prometheus-grafana-loki-logging-service", "message" : "[{}] Services, Alert : {}".format(
                                            request_json.get("env"),
                                            request_json.get("log_status")
                                            ), 
                                            "env" : "{}".format(request_json.get("env")), 
                                            }},
                )

            return {"message": "Inserted log successfully."}
          
            ''' --------------- '''
        except Exception as e:
           self.logger.error(e)
           return StatusException.raise_exception(str(e))
