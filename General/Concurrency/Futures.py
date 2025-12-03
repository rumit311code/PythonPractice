"""
Python's concurrent.futures module provides a simple and powerful way to run tasks concurrently
using threads or processes. Below are sample code snippets showing different patterns of usage
for both thread-based and process-based parallelism, focusing on practical examples for real-world problems.
"""
import concurrent.futures
import time
import random

"""
ThreadPoolExecutor: Running Tasks Concurrently.
This example demonstrates how to use ThreadPoolExecutor to execute tasks concurrently and 
retrieve results in the ORDER of COMPLETION "futures.as_completed".
This processes results as soon as they finish, allowing early handling of fast jobs.
"""
def mail_letter(letter):
    duration = random.randint(1, 5)
    print(f"Started mailing letter {letter} (duration: {duration}s)")
    time.sleep(duration)
    print(f"Finished mailing letter {letter}")
    return f"Letter {letter} mailed"

letters = ['A', 'B', 'C', 'D', 'E']
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(mail_letter, letter): letter for letter in letters}
    for future in concurrent.futures.as_completed(futures):
        letter = futures[future]
        result = future.result()
        print(f"Result: {result}")


"""
ThreadPoolExecutor: Using "executor.map" for Ordered Results
You can use executor.map if result order must match SUBMISSION ORDER.
This prints results in the same order as the original list, regardless of task completion order.
"""
def mail_letter2(letter):
    duration = random.randint(1, 5)
    time.sleep(duration)
    return f"Letter {letter} mailed"

letters = ['A', 'B', 'C', 'D', 'E']
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(mail_letter2, letters))
    for result in results:
        print(result)

"""
ProcessPoolExecutor: Parallel CPU-bound Tasks
For computationally intensive operations, use ProcessPoolExecutor:
This launches child processes to use multiple CPU cores.
"""
def compute(x):
    return x * x

nums = [1, 2, 3, 4, 5]
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = list(executor.map(compute, nums))
    print(results)  # Output: [1, 4, 9, 16, 25]

"""
Real-world Example: Downloading Web Pages in Parallel
This shows how to handle IO-bound tasks using futures for non-blocking results.
"""
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/', 'http://www.cnn.com/', 'http://europe.wsj.com/']

def load_url(url, timeout=10):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = {executor.submit(load_url, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f"{url} generated an exception: {exc}")
        else:
            print(f"{url} page is {len(data)} bytes")

