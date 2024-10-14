from config.log_config import create_log
from dotenv import load_dotenv
# import yaml
import json
import os
from service.es_log_handler import ESLogPushHandler

load_dotenv()
    
# Initialize & Inject with only one instance
logger = create_log()


"""
''' get all hots '''
hosts = read_config_json("./repository/config.json")
''' hosts = ['localhost', 'dev',...] '''
logger.info(list(hosts))
# es_hosts_enum_list =list(hosts.keys())
"""

ESLogPushHandlerInject = ESLogPushHandler(logger)