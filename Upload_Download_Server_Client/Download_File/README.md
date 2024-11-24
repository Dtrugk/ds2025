# Server-Client Communication 
## Overview
- Đây là một project về việc giao tiếp giữa server và client
## Installation

- Clone Repo về máy
```powershell
git clone https://github.com/Dtrugk/ds2025.git
cd ds2025
```

- Cài đặt các thư viện cần thiết bằng lệnh sau:
```powershell
pip install -r requirements.txt
```

## Description
### Server

- Có chức năng nhận dữ liệu từ client và save dữ liệu 
- Có chức năng gửi dữ liệu cho client
- Có chức năng list các dữ liệu client đã gửi lên 

### Client

- Có chức năng gửi dữ liệu lên server
- Có chức năng nhận dữ liệu từ server
- Có chức năng xem dữ liệu đã gửi lên server

## Usage

- Chạy file Multi-Server.py để khởi tạo server
```powershell
python /Server/Multi-Server.py
```
Sau khi chạy file Multi-Server.py, server sẽ chạy ở địa chỉ localhost và port default 9669 
```text
[+] Listening... on ('192.168.217.1', 9669)
```

- Chạy file Client.py để khởi tạo client kèm với parameter 
```powershell
python /Client/Client.py
```
- Parameter:
  - -u, --upload: upload file lên server
  - -d, --download: download file từ server về client
  - -l, --list: list các file đã upload lên server
```
usage: Client.py [-h] [-u file_name] [-d file_name] [-l]
Client for File Transfer

options:
  -h, --help            show this help message and exit
  -u file_name, --upload file_name
                        Upload a file to the server
  -d file_name, --download file_name
                        Download a file from the server
  -l, --list            List files on the server
  
Eg: python Client.py -u test.txt
    python Client.py -l 
    python Client.py -d test.txt
  ```

File sent successfully