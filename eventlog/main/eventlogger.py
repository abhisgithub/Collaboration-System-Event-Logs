import time
import datetime
import json
import urllib3
from . import logprocess
from . import settings

class StoreLog:

    def __init__(self):
        self.LOG_CLASS = "StoreLog"
        self.method = settings.LOG_TYPE
        if self.method == STORE:
             self.conf = settings.STORE_CONF
        elif self.method == TOSERVER:
            self.conf = settings.SERVER_CONF
            
    def run(self, logVal):
        if self.method == STORE:
            self._store_file(logVal)
        elif self.method == TOSERVER:
            self._to_server(logVal)

    def _to_server(self, logVal):
        pass

    def _store_file(self, logVal):
        with open(self.conf['filename'], 'a') as fp:
             fp.write(json.dumps(logVal))
            
def create_log(event_name, data):
    dic = {}
    
    # APPENDING COMMON FIELDS
    for key in list(settings.COMMON_FIELDS.keys()):
        f = settings.COMMON_FIELDS[key]
        dic[key] = f(data)

    event_specific = {}
    for key in list(settings.CONTEXT_SPECIFIC_FIELDS[event_name].keys()):
        f = settings.CONTEXT_SPECIFIC_FIELDS[event_name][key]
        #print(f.__name__)
        event_specific[key] = f(data)

    dic["event"] = event_specific
    print(dic)
    
    return dic
