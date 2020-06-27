import requests
import socket
statuscode="<Response [200]>"
localhost = socket.gethostbyname('localhost')
request = requests.get("http://www.google.com")
response=request.status_code
def check_localhost():
    if localhost == "127.0.0.1":
        return True
    else:
        return False
def check_connectivity():
    if response == 200:
        return True
    else:
        return False
print(check_localhost())
print(check_connectivity())
