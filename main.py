import argparse
from zoo.testset import TestSet

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("-p", "--port", type=int)
    parser.add_argument("size", type=str)
    parser.add_argument("n_threads", type=int)
    args = parser.parse_args()
    if not args.port:
        test = TestSet(args.host, 2181, args.size, args.n_threads)
    else:
        test = TestSet(args.host, args.port, args.size, args.n_threads)
    test.start_all()

if __name__ == "__main__":
    main()