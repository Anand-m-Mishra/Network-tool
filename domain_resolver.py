import socket
from logger import log_action  # Import the updated log_action function

def resolve_domain(domain):
   
    log_action("Domain resolution started", f"Attempting to resolve domain: {domain}", "info")
    
    try:
        ip_address = socket.gethostbyname(domain)
        log_action("Domain resolved", f"Domain {domain} resolved to IP: {ip_address}", "info")
        return ip_address
    except socket.gaierror as e:
        error_message = f"Failed to resolve domain {domain}: {e}"
        log_action("Domain resolution error", error_message, "error")
        return error_message
