import socket
import json
from tabulate import tabulate

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9669
SIZE = 1024
FORMAT = 'utf-8'
ADDR = (HOST, PORT)


def list_file():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    msg = '<list>_Please-Send-Files-list'
    client.send(msg.encode(FORMAT))

    try:
        file_list = client.recv(SIZE).decode(FORMAT)
    except Exception as e:
        print(f"Client Error: {e}")

    file_details = json.loads(file_list)
    # Prepare the data for tabulation
    table_data = [(file_info['name'], f"{file_info['size']} bytes", file_info['type']) for file_info in file_details]

    # Define the table headers
    headers = ["Name", "Size", "Type"]

    # Use tabulate to format the table
    table = tabulate(table_data, headers, tablefmt="grid")
    print("List of files on the server with details:")
    print(table)
    client.close()
