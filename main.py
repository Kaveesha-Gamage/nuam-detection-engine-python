import subprocess
from threading import Thread
from network.topology import create_lab_network
from network.runner import generate_test_traffic
from mininet.cli import CLI
import time
import sys

if __name__ == "__main__":
    from mininet.log import setLogLevel
    setLogLevel("info")

    #Start Mininet network
    net = create_lab_network()

    #Start traffic generation in a thread (on VM host)
    traffic_thread = Thread(
        target=generate_test_traffic,
        args=(net,),
        daemon=True
    )
    traffic_thread.start()

    #Start detection engine inside hIDS host
    hIDS = net.get('hIDS')
    print("*** Starting detection engine on hIDS")
    
    hIDS_proc = hIDS.popen(
        "sudo -E python3 /media/sf_shared/start_detection.py",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    
    while True:
        line = hIDS_proc.stdout.readline()
        if line:
            print("[hIDS]", line.decode().strip())
        elif hIDS_proc.poll() is not None:
            print("Detection engine stopped!")
            break
                
    CLI(net)

    #Stop network on exit
    net.stop()
