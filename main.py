import argparse

from ping import ping
from resource_monitor import networkCheck
from uptime_check import checkWeb

def main():
    parser = argparse.ArgumentParser(description = "Network monitoring tool")
    parser.add_argument("--ping",help="ping a host using ping command. Learn more at https://www.ibm.com/docs/en/zvm/7.4?topic=network-ping-command")
    parser.add_argument("--web",help="check the uptime of the website")
    parser.add_argument("--network",help="check the network resource usage")

    args = parser.parse_args()

    if args.ping:
        ping(args.ping)
    elif args.web:
        checkWeb(args.web)
    elif args.network:
        networkCheck()
    else:
        print("No arguments provided. Please use --help for more information.")

if __name__ == "__main__":
    main()


