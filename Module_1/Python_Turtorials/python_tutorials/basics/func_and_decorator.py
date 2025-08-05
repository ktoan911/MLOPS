# Import the library
import argparse

# Import process_time to calculate the real amount
# of time spent on this process, please take a look
# at the below articles to understand the difference
# between time(), perf_counter(), and process_time()
# https://www.linkedin.com/pulse/timetime-vs-timeperfcounter-python-raghavendraa-battula/
# https://sentry.io/answers/measure-elapsed-time-in-python/
from time import process_time

from loguru import logger

# Reference: https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-iii-decorators-with-arguments
# and take a look at this article for decorators with classes https://www.freecodecamp.org/news/python-decorators-explained-with-examples/
def measure_execution_time_with_args(*d_args, **d_kwargs):
    def wrapper(input_func):
        def inner(*args, **kwargs):
            # Calculate the starting time
            start = process_time()
            # Execute the inner function
            print("Debugging measure_execution_time arguments:")
            print("d_args: ", d_args)
            print("d_kwargs: ", d_kwargs)
            result = input_func(*args, **kwargs)
            # Calculate the end time
            end = process_time()
            #logger.info(f"Elapsed time: {end - start}")
            print(input_func)
            return result

        return inner

    return wrapper


def measure_execution_time(input_func):
    def inner(*args, **kwargs):
        # Calculate the starting time
        start = process_time()
        # Execute the inner function
        result = input_func(*args, **kwargs)
        # Calculate the end time
        end = process_time()
        logger.info(f"Elapsed time: {end - start}")
        return result

    return inner

# You can also replace with the decorator with arguments below
@measure_execution_time_with_args(10, myarg=100, myarg2=200)
#@measure_execution_time  # tương đương measure_execution_time(predict(x))
def predict(x):
    print(x)
    model = {"a": 1, "b": 2}
    logger.info("Getting predictions!")
    if x in model:
        return model[x]
    else:
        raise ValueError(f"Could not predict {x}")


def main(args):
    x = args.x
    print(predict(x))


# This is only executed when invoking this script
if __name__ == "__main__":
    # Create a parser to receive the command line arguments
    parser = argparse.ArgumentParser()
    # Define all arguments
    parser.add_argument("-x", type=str, required=True)
    # Parse the arguments
    args = parser.parse_args()
    # Run the main function
    main(args)
