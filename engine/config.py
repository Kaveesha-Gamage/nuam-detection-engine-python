from detector.ARPDetector import ARPDetector
from detector.IPDetector import IPDetector
from detector.TCPIPDetector import TCPIPDetector
import os



ENABLED_DETECTORS = {
    "ARP": ARPDetector(),
    "IP": IPDetector(),
    "TCP-IP": TCPIPDetector(),
}

BACKEND_WS_URL = os.getenv("BACKEND_WS_URL", "ws://192.168.56.1:8000/ws/device")
LOG_PATH = os.getenv("LOG_PATH", "/media/sf_shared/logs.txt")