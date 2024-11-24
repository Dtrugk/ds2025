import socket
from tqdm import tqdm
import os

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9669
SIZE = 1024
FORMAT = 'utf-8'
ADDR = (HOST, PORT)


def handle_upload(conn: socket, data: str):
    file = data.split('_')
    FILENAME = file[1]
    FILESIZE = int(file[2])

    # Sanitize filename
    Sanitize_filename = os.path.basename(FILENAME)

    # Construct the full file path for the received file
    received_file_path = os.path.join("Server", "File_storage", Sanitize_filename)

    print(f"[+] Filename and filesize received from the client. Saving as {received_file_path}")
    conn.send("Filename and filesize received".encode(FORMAT))

    bar = tqdm(total=FILESIZE, desc=f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(received_file_path, "wb") as f:
        while True:
            data = conn.recv(SIZE)
            if not data:
                break
            f.write(data)
            bar.update(len(data))

    conn.send("Data received.".encode(FORMAT))
