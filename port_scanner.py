import socket
from logger import log_action  

def scan_ports(host, start_port, end_port):
  
    open_ports = []
    log_action("Starting port scan", f"Scanning ports from {start_port} to {end_port} on {host}", "info")
    
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)  # Timeout for each connection attempt
                if sock.connect_ex((host, port)) == 0:  # 0 means the port is open
                    open_ports.append(port)
                    log_action("Port found", f"Port {port} is open on {host}", "info")
        except Exception as e:
            log_action("Port scan error", f"Error scanning port {port}: {e}", "error")
    
    log_action("Port scan completed", f"Open ports on {host}: {open_ports}", "info")
    return open_ports
