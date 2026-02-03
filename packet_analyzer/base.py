
from handler.event_handler import EventTypeHandler
from logger.logger import Logger

class BaseAnalyzer:
    
    def __init__(self, logger:Logger , event_type_handler: EventTypeHandler):
        self.logger = logger
        self.event_type_handler = event_type_handler
    
    def analyze(self, known_devices):
        raise NotImplementedError("Subclasses must implement this method")
    
    def log_analysis_event(self, seq_number, event_type , details):
        out_event =  self.event_type_handler.handle_event_type(event_type, details, seq_number)
        self.logger.send_event(out_event)

    