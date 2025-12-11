"""
Python's concurrent.futures module provides a simple and powerful way to run tasks concurrently
using threads or processes. Below are sample code snippets showing different patterns of usage
for both thread-based and process-based parallelism,
focusing on practical examples for real-world problems.

Mutual exclusion ensures only one thread accesses a shared resource at a time in multi-threading,
preventing race conditions.

Progressiveness means if no thread holds a resource and some want it, one will get it without indefinite postponement.

Non-preemptive scheduling lets a thread run until it voluntarily yields, blocks, or finishes. The lock thread puts
here is also called "mutex".

Preemptive scheduling: the OS can interrupt and stop it.

"Ranking" likely refers to priority or wait ranking in deadlock avoidance, like the banker's algorithm,
assigning resource ranks to prevent unsafe states.

Deadlocks need four conditions:
- mutual exclusion (resource non-sharable),
- hold-and-wait (holding while requesting)
- no preemption (can't force release)
- circular wait (thread cycle).

Usage in Deadlocks
- Non-preemption contributes to deadlocks by blocking forced resource release, fixable via preemption or timeouts.
- Ranking breaks circular wait by imposing a total order (e.g., lock A before B always),
ensuring requests follow ranks to avoid cycles.

Rankin + Preemptive
In non-preemptive resource access, a thread holding a resource (like a lock or mutex) cannot be interrupted or forced
to release it, even by a higher-priority thread. The lower-rank thread must voluntarily release the resource
after completing its critical section.

Scenario1:
- first thread which is non-preemptive, but LOWER rank holds a resource.
- second thread which is preemptive, but HIGHER rank request for the same resource.
- Outcome: this scenario does not constitute a deadlock. Deadlock requires mutual blocking among
multiple threads in a circular wait, along with mutual exclusion, hold-and-wait, and no preemption;
here, only the higher-priority thread waits indefinitely while the lower-priority one holds the resource
without waiting for anything else.
- Problem Type: This is unbounded priority inversion, not deadlock, where the low-priority thread
(non-preemptive on the resource) blocks the high-priority one indefinitely if it never exits
its critical section—possibly due to a bug, infinite loop, or excessive computation.

## Resolution Strategies
- **Timeouts**: Higher-priority thread uses timed waits on the resource; upon timeout,
    it aborts or escalates (e.g., via watchdog timers in real-time systems).
- **Priority Inheritance/Ceiling Protocols**: Temporarily boost the holder's priority to match the highest waiter,
    ensuring it completes quickly without intervention.
- **Preemption or Forced Release**: Rare in user-space; kernel may intervene for non-preemptable resources
    via signals or process termination if configured.
- **Design Prevention**: Use short critical sections, avoid nested locks, and employ hierarchical locking
    to eliminate cycles.

Short critical sections minimize the time a thread holds a shared resource, reducing blocking and contention risks.

## Short Critical Sections
- Critical sections are code segments accessing shared resources like variables or files,
protected by locks (e.g., mutexes) for mutual exclusion. Keeping them short means performing only essential
operations inside—avoid I/O, complex computations, or loops—to limit hold time, prevent priority inversion,
and improve system responsiveness.

## Hierarchical Locking
This technique imposes a strict total order on resources (e.g., by address or ID), requiring threads to
always acquire locks in that sequence. It breaks circular wait conditions for deadlock prevention:
lower-ID lock first, then higher-ID. Example: Lock A (ID 1) before B (ID 2) across all threads.

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
# def mail_letter2(letter):
#     duration = random.randint(1, 5)
#     time.sleep(duration)
#     return f"Letter {letter} mailed"

letters = ['A', 'B', 'C', 'D', 'E']
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(mail_letter, letters))
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
    # results = list(executor.map(compute, nums))
    results = executor.map(compute, nums)
    for result in results:
        print(f"result ---> {result}")
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

