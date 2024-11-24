import socket
from tqdm import tqdm
import os

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9669
SIZE = 2048
FORMAT = 'utf-8'
ADDR = (HOST, PORT)


def handle_download(conn: socket, data: str):
    file = data.split('_')
    FILENAME = file[1]

    file_path = f"D:\\Red-Team\\Write-Up\\Client_Server\\Upload_Download_Server_Client\\Server\\File_storage\\{FILENAME}"
    if os.path.isfile(file_path):
        conn.send("File exists".encode(FORMAT))

        # Get the file size and send it to the client
        FILESIZE = os.path.getsize(file_path)
        file_info = f"{FILENAME}_{FILESIZE}"
        conn.send(file_info.encode(FORMAT))

        bar = tqdm(total=FILESIZE, desc=f"[+] Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

        with open(file_path, "rb") as f:
            while True:
                data = f.read(SIZE)
                if not data:
                    break
                conn.send(data)
                bar.update(len(data))
            print('Finish')
        conn.send("File sent successfully".encode(FORMAT))
        conn.close()
    else:
        conn.send("File not found".encode(FORMAT))
