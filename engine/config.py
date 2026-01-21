from detector.ARPDetector import ARPDetector
from detector.IPDetector import IPDetector

ENABLED_DETECTORS = {
    "ARP": ARPDetector(),
    "IP": IPDetector(),
}

BACKEND_BASE_URL = "http://192.168.56.1"
BACKEND_PORT = 5000