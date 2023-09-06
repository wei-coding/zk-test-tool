from kazoo.client import KazooClient
from kazoo.exceptions import KazooException
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
    bad_counter = 0
    write_counter = 0
    start_time = time.time()
    now_time = start_time
    total_latency = 0
    while (now_time - start_time < time_limit):
        try:
            if random.random() > read_portion:
                latency = time.time()
                zk.set(f"/read_write_test/{name}", value=b"x"*parse(size))
                latency = time.time() - latency
                total_latency += latency
                write_counter += 1
            else:
                zk.get(f"/read_write_test/{name}")
        except KazooException as e:
            print(e)
            bad_counter += 1
        
        counter += 1
        now_time = time.time()
    zk.stop()
    with open("data/"+log_name+".log", "a+") as f:
        print(f"{counter//30} {total_latency/write_counter} {bad_counter} {counter}", file=f)