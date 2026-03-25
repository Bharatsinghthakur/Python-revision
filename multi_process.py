import multiprocessing
import time

def do_something(seconds):
    print(f'Sleeping in {seconds} second(s) ..')
    time.sleep(seconds)
    print('Done Sleeping ...')

# we have to pass the function not the return value of its i.e function()
start = time.perf_counter()
if __name__ == '__main__':
    processes = []
    # to run multiple process at same time 
    for _ in range(10):

        p = multiprocessing.Process(target=do_something,args=[1.5])
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()
    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()
    
finish = time.perf_counter()
print(f'Finished in {round(finish - start,2)} second(s)')

