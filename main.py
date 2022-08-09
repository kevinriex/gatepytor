from socket import timeout
from torpy import TorClient
from torpy.utils import recv_all
from torpy.http import requests
from torpy.http.adapter import TorHttpAdapter

def socket():
    with TorClient() as tor:
        with tor.create_circuit(3) as circ:
            with circ.create_stream((host,80)) as stream:
                stream.send(b"GET / HTTP/1.0\r\nHost: %s\r\n\r\n" % host.encode())
                ret = recv_all(stream).decode()
                print(ret)

def request():
    with TorClient() as tor:
        with tor.get_guard() as guard:
            adapter = TorHttpAdapter(guard, 3)
            with requests.Session() as session:
                session.headers.update({'User-Agent':'Mozilla/5.0'})
                session.mount('http://', adapter)
                session.mount('https://', adapter)

                resp = session.get(host, timeout=15)
                print(resp.text)

                resp = session.get(host2, timeout=15)
                print(resp.text)



if __name__ == "__main__":
    host = "http://facebookcorewwwi.onion"
    host2 = "http://ifconfig.me"
    #socket()
    request()