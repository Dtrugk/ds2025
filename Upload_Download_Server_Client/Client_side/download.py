import os
import socket
from tqdm import tqdm

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9669
ADDR = (HOST, PORT)
SIZE = 2048
FORMAT = "utf-8"


def download_file(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    client.send(f"<download>_{filename}".encode(FORMAT))

    confirmation = client.recv(SIZE).decode(FORMAT)

    if confirmation == "File exists":
        # ----------------------------------------------------
        file_info = client.recv(SIZE).decode(FORMAT)
        file = file_info.split("_")
        file_size = int(file[1])
        file_name = file[0]
        file_name.replace("/.\,.", " ")
        print(f'[+] File name: {file_name}\n[+] File size: {file_size} Bytes')

        download_file_path = os.path.join("D:\\Red-Team\\Write-Up\\Client_Server\\Upload_Download_Server_Client"
                                          "\\Download_File\\",
                                          filename)
        bar = tqdm(total=file_size, desc=f"[+] Receiving {filename}", unit="B", unit_scale=True, unit_divisor=SIZE)
        # ---------------------------------------------------
        with open(download_file_path, "wb") as f:
            try:
                while True:
                    data = client.recv(SIZE)
                    if not data:
                        break
                    f.write(data)
                    bar.update(len(data))

                print(f"[+] Received {filename}")
                closing_signal = client.recv(SIZE).decode(FORMAT)
                if closing_signal == "File sent successfully":
                    client.close()
            except Exception as e:
                print(f"[-] Error during download: {e}")
                client.close()
    else:
        print(f"[-] File '{filename}' not found on the server.")
