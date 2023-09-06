from kazoo.client import KazooClient
import time
from . import parse_size

def zoo_client(hosts, port = 2181, name = "a", size = "1K", times=30, logname="testset.log"):
    hosts_str = ",".join([f"{h}:{port}" for h in hosts])
    zk = KazooClient(hosts=hosts_str)
    zk.start()
    for i in range(times):
        f = open("data/"+logname, "a+")
        log_str = f"/{name}{i}{name} {time.time()}"
        zk.create(f"/{name}{i}{name}", (i%10).to_bytes(1, 'big') * parse_size.parse(size))
        log_str += f" {time.time()}"
        print(log_str, file=f)
        f.close()
        time.sleep(1)
    zk.sync(f"/{name}{times-1}{name}")
    zk.stop()

if __name__ == "__main__":
    zoo_client("10.10.1.1", size="1000K", times=1)