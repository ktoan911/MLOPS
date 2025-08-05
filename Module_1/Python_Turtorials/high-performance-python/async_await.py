import asyncio
 
# Define the 1st coroutine to download the 1st dataset
async def download_my_1st_data_func():
    print("Starting my 1st data func...")
    # The current coroutine is blocked for 5 seconds,
    # but other coroutines should not be blocked
    await asyncio.sleep(5)
    print("Completed my 1st data func!")

# Define the 2nd coroutine to download the 2nd dataset
async def download_my_2nd_data_func():
    print("Starting my 2nd data func...")
    # The await keyword will pause the current coroutine
    await asyncio.sleep(1)
    print("Completed my 2nd data func!")
 
async def main():
    # # 1. Execute coroutines sequentially
    # await download_my_1st_data_func()
    # await download_my_2nd_data_func()

    # 2. Execute coroutines concurrently
    task_1 = asyncio.create_task(download_my_1st_data_func())
    task_2 = asyncio.create_task(download_my_2nd_data_func())

    await task_1
    await task_2

# Start the event loop by using asyncio
# this one is a high-level concept
# of asyncio.get_event_loop()
asyncio.run(main())
