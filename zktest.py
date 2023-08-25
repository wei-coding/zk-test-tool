import argparse
from zoo.testset import TestSet

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("-p", "--port", type=int)
    parser.add_argument("-s", "--start", type=int)
    parser.add_argument("size", type=str)
    parser.add_argument("n_threads", type=int)
    parser.add_argument("name", type=str)
    parser.add_argument("-I", "--id", type=str)
    args = parser.parse_args()

    log_filename = args.name + args.id if args.id else args.name
    port = args.port if args.port else 2181
    if args.start:
        test = TestSet(args.host, port, args.size, args.n_threads, args.start, log_filename)
    else:
        test = TestSet(args.host, port, args.size, args.n_threads, 0, log_filename)
    test.start_all()

if __name__ == "__main__":
    main()