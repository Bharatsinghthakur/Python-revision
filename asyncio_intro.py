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
    sync_result = sync_function("Test")
    print(sync_result)

# To start a event loop for any of our async code to work
if __name__ == "__main__":
    asyncio.run(main())

