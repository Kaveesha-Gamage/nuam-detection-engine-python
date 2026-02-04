from scapy.all import ARP, IP, TCP, UDP, ICMP, DNS

class DetectionEngine:
    def __init__(self , detectors):
        self.detectors = detectors
        
    def observe_type(self, packet):
    
        if ARP in packet:
            return "ARP"

        elif IP in packet and TCP in packet:
            return "TCP-IP"

        elif IP in packet:
            return "IP"

        elif TCP in packet:
            return "TCP"

        elif UDP in packet:
            return "UDP"

        elif ICMP in packet:
            return "ICMP"

        elif DNS in packet:
            return "DNS"

        return None
    
    
    def extract_device_info(self , packet , observed_type):
        details = self.detectors[observed_type].extract_details(packet)
        return details , observed_type