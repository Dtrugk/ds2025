import socket
import os
import json

SIZE = 2048
FORMAT = 'utf-8'


def get_file_details(directory):
    # List files in the specified directory
    files = os.listdir(directory)

    # Create a list to store file details
    file_details = []

    for file_name in files:
        file_path = os.path.join(directory, file_name)
        file_stat = os.stat(file_path)
        file_size = file_stat.st_size
        file_mtime = file_stat.st_mtime

        # Append file details to the list
        file_details.append({
            'name': file_name,
            'size': file_size,
            'mtime': file_mtime,
            'type': 'file' if os.path.isfile(file_path) else 'directory'
        })

    return file_details


def handle_list_files(conn: socket):
    # Get detailed file information
    file_details = get_file_details(
        'D:\\Red-Team\\Write-Up\\Client_Server\\Upload_Download_Server_Client\\Server\\File_storage\\')

    # Print path
    print(f"File locate at: {file_details}\n")
    print("\n")

    # Convert the file details to a JSON string
    file_details_json = json.dumps(file_details)

    # Send the list of files to the client
    file_list_details = file_details_json

    # conn.send(file_list.encode(FORMAT))
    conn.send(file_list_details.encode(FORMAT))
    conn.close()
