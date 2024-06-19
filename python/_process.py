import multiprocessing
import threading
import argparse
import random

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--bid')  
    args = parser.parse_args()
    print("I'm in BASH fork: " + str(args.bid))

    try:
        def example(x, tid, pid):
            print("================= BEGIN bashfork: " + str(args.bid) + " pid: " + str(pid) + " tid: " + str(tid) + " example() =================")
            for y in range(0, x):
                print(str(y) + " in bashfork: " + str(args.bid) + " pid: " + str(pid) + " tid: " + str(tid))
            print("================= END bashfork: " + str(args.bid) + " pid: " + str(pid) + " tid: " + str(tid) + " example() =================")

        def t_example(pid):
            t_one = threading.Thread(target=example, args=(random.randint(0, 10),'t_one', pid,))
            t_one_data = threading.local()
            t_one_data.x = random.randint(-999, -1) # But data can be made Thread-specific
            print(str(args.bid) + "." + pid + ".t_one thread local data: " + str(t_one_data.x))
            t_one.run()

            t_two = threading.Thread(target=example, args=(random.randint(0, 10),'t_two', pid,))
            t_two_data = threading.local()
            t_two_data.x = random.randint(-999, -1) # But data can be made Thread-specific
            print(str(args.bid) + "." + pid + ".t_two thread local data: " + str(t_two_data.x))
            t_two.run()


        def p_example(pid):
            p = multiprocessing.Process(target=t_example, args=(pid,))
            p.start()
            # p.join() # Blocking

        p_example('p_one')

        p_example('p_two')

    except Exception as ex:

        print('Exception: ' + str(ex))