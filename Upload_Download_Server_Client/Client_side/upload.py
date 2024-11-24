import os
import socket
from tqdm import tqdm

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9669
ADDR = (HOST, PORT)
SIZE = 1024
FORMAT = "utf-8"


def upload(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    FILESIZE = os.path.getsize(filename)
    file_info_1 = f"<upload>_{filename}_{FILESIZE}"
    client.send(file_info_1.encode(FORMAT))

    bar = tqdm(total=FILESIZE, desc=f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(filename, "rb") as f:
        while True:
            data = f.read(SIZE)
            if not data:
                break
            client.send(data)
            bar.update(len(data))

    confirmation = client.recv(SIZE).decode(FORMAT)
    if confirmation == 'Data received.':
        print('Done! Closing connection')
        client.close()
    else:
        pass


