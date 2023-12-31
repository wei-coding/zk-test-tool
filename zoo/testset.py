import threading
from .connection import zoo_client
from .stress_test import zoo_read_write_test
from .name_gen import NameGenerator

class TestSet:
    def __init__(self, host, port, size, n_thread, start=0, logname="testset") -> None:
        self.client_list: list[threading.Thread] = []
        ng = NameGenerator(n_thread, start)
        open("data/"+logname+".log", "w")
        for _ in range(n_thread):
            t = threading.Thread(target=zoo_client, args=(host, port, ng.next(), size, 30, logname+".log"))
            self.client_list.append(t)
    
    def start_all(self):
        for t in self.client_list:
            t.start()
        for t in self.client_list:
            t.join()

class StressTestSet:
    def __init__(self, host, port, size, n_thread, start=0, read_portion=0.0, logname="stress_testset") -> None:
        self.client_list: list[threading.Thread] = []
        self.logname = logname
        open("data/"+logname+".log", "w")
        for i in range(n_thread):
            t = threading.Thread(target=zoo_read_write_test, args=(host, port, f"t-{start+i}", size, 30, read_portion, logname))
            t.setName(f"Thread-{i}")
            self.client_list.append(t)
    
    def start_all(self):
        for t in self.client_list:
            t.start()
        for t in self.client_list:
            t.join()
