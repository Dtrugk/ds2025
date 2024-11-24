import socket
import argparse
import os
import threading
from File_list import *
from Handle_upload import *
from Handle_download import *

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9669
SIZE = 2048
FORMAT = 'utf-8'
ADDR = (HOST, PORT)


def handle_client(conn, addr):
    print(f"[+] Client connected from {addr[0]}:{addr[1]}")

    data = conn.recv(SIZE).decode(FORMAT)
    parts = data.split('_')
    if len(parts) >= 1:
        command = parts[0]
        if command == "<upload>" and len(parts) >= 2:
            handle_upload(conn, data)
        elif command == "<list>":
            handle_list_files(conn)
        elif command == "<download>" and len(parts) >= 2:
            handle_download(conn, data)

    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Server for File Transfer")
    parser.add_argument("--dir", default="Server/File_storage", help="Directory to store received files")
    parser.add_argument("--port", "-p", type=int, default=9669, help="Port for server")
    args = parser.parse_args()

    RECEIVE_DIR = args.dir

    os.makedirs(RECEIVE_DIR, exist_ok=True)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[+] Listening... on {ADDR}")

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()


if __name__ == "__main__":
    main()
