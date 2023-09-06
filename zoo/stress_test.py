from kazoo.client import KazooClient
import time
import random
from zoo.parse_size import parse

def zoo_read_write_test(hosts, port = 2181, name='a', size='1K', time_limit=30, read_portion=0, log_name='stress_testset.log'):
    hosts_str = ",".join([f"{h}:{port}" for h in hosts])
    zk = KazooClient(hosts=hosts_str)
    zk.start()
    zk.ensure_path("/read_write_test")
    zk.create(f"/read_write_test/{name}", value=b"x"*parse(size), ephemeral=True)
    random.seed(time.time())
    counter = 0
    start_time = time.time()
    now_time = start_time
    while (now_time - start_time < time_limit):
        if random.uniform(0.0, 1.0) < read_portion:
            zk.set(f"/read_write_test/{name}", value=b"x"*parse(size))
        else:
            zk.get(f"/read_write_test/{name}")
        counter += 1
        now_time = time.time()
    zk.stop()
    with open("data/"+log_name+".log", "a+") as f:
        print(f"{counter//30}", file=f)