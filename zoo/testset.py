import threading
from .connection import zoo_client
from .name_gen import NameGenerator

class TestSet:
    def __init__(self, host, port, size, n_thread) -> None:
        self.client_list: list[threading.Thread] = []
        ng = NameGenerator(n_thread)
        for _ in range(n_thread):
            t = threading.Thread(target=zoo_client, args=(host, port, ng.next(), size, 30))
            self.client_list.append(t)
    
    def start_all(self):
        for t in self.client_list:
            t.start()
        for t in self.client_list:
            t.join()