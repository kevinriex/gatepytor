from torpy import TorClient
from torpy.utils import recv_all

def main():
    host = "http://facebookcorewwwi.onion"
    host = "ifconfig.me"
    with TorClient() as tor:
        with tor.create_circuit(3) as circ:
            with circ.create_stream((host,80)) as stream:
                stream.send(b"GET / HTTP/1.0\r\nHost: %s\r\n\r\n" % host.encode())
                ret = recv_all(stream).decode()
                print(ret)


if __name__ == "__main__":
    main()