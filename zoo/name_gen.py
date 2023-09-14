class NameGenerator:
    def __init__(self, n, start=0) -> None:
        self.name_list = []
        self.idx = -1
        for i in range(n):
            idx = start + i
            if idx // 26 == 0:
                self.name_list.append(chr(ord('a') + idx))
            else:
                self.name_list.append(chr(ord('a') + (idx // 26 - 1)) + chr(ord('a') + idx % 26))
        # print(self.name_list)

    def next(self):
        self.idx += 1
        if self.idx == len(self.name_list):
            raise EOFError()
        return self.name_list[self.idx]
    
if __name__ == "__main__":
    ng = NameGenerator(100, 60)