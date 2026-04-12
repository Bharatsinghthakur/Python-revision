# ASYNC IO 

import asyncio
import time

def sync_function(test_param:str) -> str:
    print("This is a synchronous function.")

    time.sleep(0.1)

    return f"Sync Result:{test_param}"

# ALSO KNOWN AS A COROUTINE FUNCTION

async def async_function(test_parm:str) -> str:
    print("This is an asynchrounous coroutine function.")

    await asyncio.sleep(0.1)

    return f"Async Result:{test_parm}"

async def main():
    # sync_result = sync_function("Test")
    # print(sync_result)


    # FUTURE -- promise like object used in low level code
    # loop = asyncio.get_running_loop()
    # future = loop.create_future() # a promise like object
    # print(f"Empty Future: {future}")

    # future.set_result("Future Result: Test")
    # future_result = await future
    # print(future_result)

    # coroutine_obj = async_function("Test")
    # print(coroutine_obj)

    # coroutine_result = await coroutine_obj
    # print(coroutine_result)

    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task 
    print(task_result)



# To start a event loop for any of our async code to work
if __name__ == "__main__":
    asyncio.run(main())

