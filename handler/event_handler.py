from datetime import datetime, timezone


class EventTypeHandler:
    
    def __init__(self):
        self.event__to_state_mapper = {
            "DEVICE_JOINED" : "TOPOLOGY"
        }
    
    def handle_event_type(self, event_type, details, seq_number):
        event = {
            "meta": {
                "timestamp": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                "sequence": seq_number,
            },
            "type": "", # STATE | METRIC | TOPOLOGY | HEALTH
            "subtype": event_type,
            "payload": details
        }
        
        if event_type == "DEVICE_JOINED":
            event["payload"] = self.handle_device_joined_event_type(details)
            event["type"] = self.event__to_state_mapper[event_type]
        elif event_type == "DEVICE_IDLE":
            event["type"] = "STATE"
            event["payload"] = self.handle_device_idle_event_type(details)
        elif event_type == "DEVICE_LEFT":
            event["type"] = "TOPOLOGY"
            event["payload"] = self.handle_device_left_event_type(details)
        elif event_type == "PERIODIC_TOPOLOGY_STATE":
            event["type"] = "TOPOLOGY"
            event["payload"] = self.periodic_topology_event_type(details)
            
        return event
        
    def handle_device_joined_event_type(self, details):
        
        event_payload = {
            "event_type": "device_connected",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "device": {
                "device_id": details["mac"],
                "hostname": details["hostname"],
                "ip_address": details["ip_address"],
                "device_type": details["device_type"],
                "os": details["os"],
                "vendor": details["vendor"],
                "first_seen": details["first_seen"],
                "last_seen":  details["last_seen"]
            },
            # "network": {
            #     "interface": details.get("interface"),
            #     "vlan": details.get("vlan"),
            #     "signal_strength": details.get("signal_strength"),  # for Wi-Fi
            #     "connection_type": details.get("connection_type", "wired")
            # }
        }
        
        return event_payload
    
    def handle_device_idle_event_type(self, details):
        
        event_payload = {
            "event_type": "device_idle",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "device": {
                "device_id": details["mac"],
                "hostname": details["hostname"],
                "ip_address": details["ip_address"],
                "device_type": details["device_type"],
                "os": details["os"],
                "vendor": details["vendor"],
                "first_seen": details['first_seen'],
                "last_seen": details["last_seen"]
            }
        }
        
        return event_payload
    
    def handle_device_left_event_type(self, details):
        event_payload = {
            "event_type": "device_disconnected",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "device": {
                "device_id": details["mac"],
                "hostname": details["hostname"],
                "ip_address": details["ip_address"],
                "device_type": details["device_type"],
                "os": details["os"],
                "vendor": details["vendor"],
                "last_seen": details["last_seen"],
                "first_seen": details['first_seen']
            }
        }
        
        return event_payload
    
    
def periodic_topology_event_type(self, details):
    event_payload = {
        "event_type": "topology_snapshot",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "topology": details
    }
    
    return event_payload