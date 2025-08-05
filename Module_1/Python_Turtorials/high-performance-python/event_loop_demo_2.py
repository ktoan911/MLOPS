# Let's say you have one process with one thread only, how to deal with it?
# AsyncIO helps us to do it
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
    await asyncio.sleep(7)
    print("Completed my 2nd data func!")

# Define the 3rd coroutine to download the 3rd dataset
async def download_my_3rd_data_func():
    print("Starting my 3rd data func...")
    await asyncio.sleep(9)
    print("Completed my 3rd data func!")

# Define a coroutine to download all the datasets
async def download_all_data_func():
    # The await keyword will pause the current coroutine
    await download_my_1st_data_func()
    await download_my_2nd_data_func()
    await download_my_3rd_data_func()

def main():
    loop = asyncio.get_event_loop()
    # await và chỉ có 1 coroutine nên phải chờ lần lượt ( )
    loop.run_until_complete(
        download_all_data_func()
    )
    loop.close()

# Run the event loop
main()