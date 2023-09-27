def parse(size_str: str) -> int:
    scaler_str = size_str[-1]
    scaler = {'K': 1000, 'M': 1000000}[scaler_str]
    number = int(size_str[:-1])
    return number * scaler

if __name__ == "__main__":
    print(parse('1K'))