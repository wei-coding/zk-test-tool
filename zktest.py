import argparse
from zoo.testset import TestSet, StressTestSet

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hostfile", type=str)
    parser.add_argument("-p", "--port", type=int)
    parser.add_argument("-s", "--start", type=int)
    parser.add_argument("size", type=str)
    parser.add_argument("n_threads", type=int)
    parser.add_argument("name", type=str)
    parser.add_argument("-I", "--id", type=str)
    stress_group = parser.add_argument_group()
    stress_group.add_argument("--stress", action="store_true", dest="stress_mode")
    stress_group.add_argument("--read", type=float, dest="read_portion")
    args = parser.parse_args()

    log_filename = args.name + args.id if args.id else args.name
    port = args.port if args.port else 2181
    args.start = args.start if args.start else 0
    hosts = []
    with open('conf/host.conf') as f:
        for l in f.readlines():
            l = l.strip()
            if l and not l.startswith('#'):
                hosts.append(l)
    if not args.stress_mode:
        test = TestSet(hosts, port, args.size, args.n_threads, args.start, log_filename)
        test.start_all()
    else:
        test = StressTestSet(hosts, port, args.size, args.n_threads, args.start, args.read_portion, log_filename)
        test.start_all()

if __name__ == "__main__":
    main()