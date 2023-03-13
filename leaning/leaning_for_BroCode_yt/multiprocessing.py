# *****************************************
# Python multiprocessing
# *****************************************
#
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound taks (heavy cpu usage)
#                   multithreading = better for io bound taks (waiting around)


from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    a = Process(target=counter, args=(100000000,))
    a.start()

    a.join()
    print("finished in: ", time.perf_counter(), "second")

if __name__ == '__main__':
    main()

