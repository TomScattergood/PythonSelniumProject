"""
Question: Write a function that will keep retrying to check a status of a process by calling
the function "is_status_success()" until the function returns True.

Retry for 20 seconds  while sleeping 3 seconds between each retry. After the 20 seconds raise an exception
if the success check is not True.
Make the max retry length and the sleep time keyword parameters to the function with default values.

The function to call to check the status is writen below. The function will randomly return True or False.
Call the function in the loop as a way of checking success status of a process.

Requirement:
    - Use while loop
    - Use timer
    - Raise an Exception
    - keyword parameter for max retry
    - keyword parameter for sleep time between retries

Hint:
    To set a timer you can import time and to set a timeout you can do
        > time.time() + 20 # this will set a timeout 20 seconds from now. time.time() is now.
"""

import random
import time


def is_status_success():
    print("Checking the status of the process.")
    list_to_chose_from = [True, True, False, False, False, False, False]

    bool_to_return = random.choice(list_to_chose_from)

    return bool_to_return


def wait_and_retry_until_success(max_wait=20, sleep_time=3):
    is_success = False
    timeout = time.time() + max_wait
    while time.time() <= timeout:
        is_success = is_status_success()
        print("Status is success: {}".format(is_success))
        is_success = is_status_success()

        if is_success:
            print("The process is successful")
            break
        else:
            print("The process is not successful, sleeping for {} seconds".format(sleep_time))
            time.sleep(sleep_time)
            continue

    else:
        raise Exception("The status did not succeed after waiting {} seconds".format(max_wait))


wait_and_retry_until_success(6, 3)
