from detector.base import Detector


class TCPIPDetector(Detector):
    def __init__(self):
        super().__init__(name="TCPIPDetector", detector_type="TCP-IP")
        
    def extract_details(self, packet):
        ip_layer = packet.getlayer("IP")
        tcp_layer = packet.getlayer("TCP")
        
        details = {
            "packet_type": "TCP-IP",
            "eth_src": packet.src,
            "eth_dst": packet.dst,
            "src_ip": ip_layer.src,
            "dst_ip": ip_layer.dst,
            "version": ip_layer.version,
            "ihl": ip_layer.ihl,
            "tos": ip_layer.tos,
            "len": ip_layer.len,
            "id": ip_layer.id,
            "flags": ip_layer.flags,
            "frag": ip_layer.frag,
            "ttl": ip_layer.ttl,
            "proto": ip_layer.proto,
            "chksum": ip_layer.chksum,
            "src_port": tcp_layer.sport,
            "dst_port": tcp_layer.dport,
            "seq": tcp_layer.seq,
            "ack": tcp_layer.ack,
            "dataofs": tcp_layer.dataofs,
            "reserved": tcp_layer.reserved,
            "flags": tcp_layer.flags,
            "window": tcp_layer.window,
            "chksum_tcp": tcp_layer.chksum,
            "urgptr": tcp_layer.urgptr,
            "is_broadcast": packet.dst == "ff:ff:ff:ff:ff:ff",
            "options": ip_layer.options,
            "data_sent": len(packet)
        }
        
        return details