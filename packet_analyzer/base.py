
from handler.event_handler import EventTypeHandler
from logger.logger import Logger

class BaseAnalyzer:
    
    def __init__(self, event_type_handler: EventTypeHandler):
        self.event_type_handler = event_type_handler
    
    def analyze(self, known_devices):
        raise NotImplementedError("Subclasses must implement this method")
    
    