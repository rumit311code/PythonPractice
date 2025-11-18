import threading
import multiprocessing
import time
import math

"""
Multithreading  I/O-bound tasks took 2.00 seconds RECOMMENDED
Multiprocessing I/O-bound tasks took 3.74 seconds
Multiprocessing CPU-bound tasks took 1.88 seconds RECOMMENDED
Multithreading  CPU-bound tasks took 4.21 seconds 
"""

# I/O-bound task (simulated with time.sleep)
def io_bound_task(name):
    print(f"{name} - Starting I/O-bound task")
    time.sleep(2)  # simulate I/O wait
    print(f"{name} - Finished I/O-bound task")

# CPU-bound task (heavy computation)
def cpu_bound_task(name):
    print(f"{name} - Starting CPU-bound task")
    result = 0
    for i in range(10**7):
        result += math.sqrt(i)
    print(f"{name} - Finished CPU-bound task")

# Run I/O-bound tasks with multithreading -> RECOMMENDED
def run_io_bound_multithreading():
    threads = []
    start_time = time.time()
    for i in range(4):
        t = threading.Thread(target=io_bound_task, args=(f"Thread-{i+1}",))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"Multithreading I/O-bound tasks took {time.time() - start_time:.2f} seconds\n")

# Run I/O-bound tasks with multiprocessing -> NOT RECOMMENDED
def run_io_bound_multiprocessing():
    processes = []
    start_time = time.time()
    for i in range(4):
        p = multiprocessing.Process(target=io_bound_task, args=(f"Process-{i+1}",))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print(f"Multiprocessing I/O-bound tasks took {time.time() - start_time:.2f} seconds\n")

# Run CPU-bound tasks with multiprocessing -> RECOMMENDED
def run_cpu_bound_multiprocessing():
    processes = []
    start_time = time.time()
    for i in range(4):
        p = multiprocessing.Process(target=cpu_bound_task, args=(f"Process-{i+1}",))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print(f"Multiprocessing CPU-bound tasks took {time.time() - start_time:.2f} seconds\n")

# Run CPU-bound tasks with multiprocessing -> NOT RECOMMENDED
def run_cpu_bound_multithreading():
    threads = []
    start_time = time.time()
    for i in range(4):
        t = threading.Thread(target=cpu_bound_task, args=(f"Thread-{i+1}",))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"Multithreading CPU-bound tasks took {time.time() - start_time:.2f} seconds\n")

if __name__ == "__main__":
    print("Running I/O-bound tasks with multithreading:")
    run_io_bound_multithreading()

    print("Running I/O-bound tasks with multiprocessing:")
    run_io_bound_multiprocessing()

    print("Running CPU-bound tasks with multiprocessing:")
    run_cpu_bound_multiprocessing()

    print("Running CPU-bound tasks with multithreading:")
    run_cpu_bound_multithreading()
