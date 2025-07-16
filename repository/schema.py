from pydantic import BaseModel
from datetime import datetime
from pytz import timezone as tz
from enum import Enum
from typing import List, Union
import uuid
import sys


class Sort_Order(str, Enum):
    desc = 'DESC'
    asc = 'ASC'
    


class Log(BaseModel):
    service: str = 'prometheus-golang-monitoring-service'
    log_status: str= "error"
    env: str = "dev"
    host: str = "localhost#1"
    host_name: str = "Data_Node_#1"
    log_filename: str = "StreamProcessExecutor.log"
    message: str = 'PROCESS proc'
        
    def to_json(self):
        return {
            'service': str(self.service),
            'log_status' : str(self.log_status).upper(),
            'env' : str(self.env).upper(),
            'host' : str(self.host),
            'host_name' : str(self.host_name),
            'log_filename' : str(self.log_filename),
            'message' : str(self.message)
        }