import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} Second(s)')
    time.sleep(seconds)
    return f'Done Sleeping ...{seconds}'

'''
 
with concurrent.futures.ThreadPoolExecutor() as executor:
   secs = [5,4,3,2,1]
#  results = [executor.submit(do_something,1) for _ in range(10)]
   results = [executor.submit(do_something, sec) for sec in secs]

   # will yield result once its finish and we can iterate it with loop
   for f in concurrent.futures.as_completed(results):
       print(f.result())

    # we have list comprehension above for this
       
    # f1 = executor.submit(do_something,1) # future object
    # f2 = executor.submit(do_something,1) 


    # print(f1.result()) # it will wait around till the function complete
    # print(f2.result()) # it will wait around till the function complete


    # we can also use map function to do the same 
    # map will return the result as in order the list values were passed
'''


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    # when we use submit method it returns the future object -- results were shown as completed
    # but when we use map it returns the result instead -- map gonna return the result the order in which they are started
    results = executor.map(do_something,secs)

    for result in results:
      print(result)

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")


