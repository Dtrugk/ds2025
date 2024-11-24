import argparse
import sys

from download import *
from list import *
from upload import *

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9669
ADDR = (HOST, PORT)
SIZE = 1024
FORMAT = "utf-8"



def main():

    parser = argparse.ArgumentParser(description="Client for File Transfer")
    parser.add_argument("-u", "--upload", metavar="file_name", help="Upload a file to the server")
    parser.add_argument("-d", "--download", metavar="file_name", help="Download a file from the server")
    parser.add_argument("-l", "--list", action="store_true", help="List files on the server")
    # Display help message if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    if args.upload:
        # Upload the specified file to the server
        client.send(f"<upload> {args.upload}".encode(FORMAT))
        upload(args.upload)

    elif args.download:
        # Download the specified file from the server
        client.send(f"<download> {args.download}".encode(FORMAT))
        download_file(args.download)

    elif args.list:
        # List files on the server
        client.send("<list>".encode(FORMAT))
        list_file()
    client.close()


if __name__ == "__main__":
    main()
