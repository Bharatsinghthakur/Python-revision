import concurrent.futures
import time

# do something functions --
def do_something(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    return f"Done Sleeping ...{seconds}"


start = time.perf_counter()
# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         secs = [5,4,3,2,1]
#         # results = [executor.submit(do_something, seconds) for _ in range(10)]
#         results = [executor.submit(do_something, sec) for sec in secs]

#         for f in concurrent.futures.as_completed(results):
#             print(f.result())

# finish = time.perf_counter()
if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        # results = [executor.submit(do_something, seconds) for _ in range(10)]
        results = executor.map(do_something,secs)

        for result in results:
            print(result)

"counter pref_function"
finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")
