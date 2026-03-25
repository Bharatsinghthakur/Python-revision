import threading

import time

start = time.perf_counter()

 
def do_something(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("Done sleeping")


"""
# we have to create thread we have 
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# we have to start the thread
t1.start()
t2.start()

# do_something()
# do_something()

# As the function is getting finshed without calculating the time .
# we can make the function wait till it complete its thread
t1.join()
t2.join()

"""
# list of threads so that we can store these and loop through

threads = []

# lets do this with more threads
for _ in range(10):
    t = threading.Thread(target=do_something,args=[1.5])
    t.start()
    # we cannot do join here as it will create the loop synchronously because its starting and running together without creating other threads
    threads.append(t)

# now we are running join on all thoose threads
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")


# efficient way of writing all this is 
# Thread pool executor

