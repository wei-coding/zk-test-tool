from kazoo.client import KazooClient
import time
from . import parse_size

def zoo_client(host, port = 2181, name = "a", size = "1K", times=30):
    zk = KazooClient(hosts=f"{host}:{port}")
    zk.start()
    for i in range(times):
        print(f"Write /{name}{i}{name}")
        zk.create(f"/{name}{i}{name}", (i%10).to_bytes(1, 'big') * parse_size.parse(size))
        time.sleep(1)
    zk.sync(f"/{name}{times-1}{name}")
    zk.stop()

if __name__ == "__main__":
    zoo_client("10.10.1.1", size="1000K", times=1)