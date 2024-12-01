import argparse
from ping import ping
from resource_monitor import networkCheck
from uptime_check import checkWeb
from domain_resolver import resolve_domain
from port_scanner import scan_ports
from logger import log_action  # Import the logging function

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Network monitoring tool")
    
    # Define the command-line arguments
    parser.add_argument("--ping", help="Ping a host using the ping command. Learn more at https://www.ibm.com/docs/en/zvm/7.4?topic=network-ping-command")
    parser.add_argument("--web", help="Check the uptime of the website")
    parser.add_argument("--network", help="Check the network resource usage")
    parser.add_argument("--resolve", help="Resolve a domain to its IP address")
    parser.add_argument("--ports", nargs=3, metavar=('HOST', 'START_PORT', 'END_PORT'), help="Scan ports on a host. Requires HOST, START_PORT, and END_PORT.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Log the start of the program
    log_action("Program started", "Network monitoring tool is running.", "info")

    # Handle different actions based on user input
    if args.ping:
        log_action("Ping action initiated", f"Pinging {args.ping}", "info")
        ping(args.ping)
    elif args.web:
        log_action("Web uptime check initiated", f"Checking uptime for {args.web}", "info")
        checkWeb(args.web)
    elif args.network:
        log_action("Network check initiated", "Checking network resource usage", "info")
        networkCheck()
    elif args.resolve:
        log_action("Domain resolution initiated", f"Resolving domain {args.resolve}", "info")
        result = resolve_domain(args.resolve)
        print(f"Resolved IP: {result}")
    elif args.ports:
        host, start_port, end_port = args.ports
        start_port = int(start_port)
        end_port = int(end_port)
        log_action("Port scan initiated", f"Scanning ports {start_port} to {end_port} on {host}", "info")
        open_ports = scan_ports(host, start_port, end_port)
        print(f"Open ports: {open_ports}")
    else:
        log_action("No arguments provided", "No command-line arguments were provided. User needs help.", "warning")
        print("No arguments provided. Please use --help for more information.")

    # Log the end of the program
    log_action("Program ended", "Network monitoring tool execution completed.", "info")

if __name__ == "__main__":
    main()



