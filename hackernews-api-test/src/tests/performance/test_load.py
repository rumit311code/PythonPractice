"""
Sample code to show the load test for the Top Stories and Items APIs.
"""
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def get_top_stories():
    url = f"{BASE_URL}/topstories.json"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def get_item(item_id):
    url = f"{BASE_URL}/item/{item_id}.json"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def get_top_story_and_its_comment(item_id):
    start_time = time.time()
    try:
        item = get_item(item_id)
        # Optionally fetch first comment
        if item and 'kids' in item and item['kids']:
            get_item(item['kids'][0])
        elapsed = time.time() - start_time
        return (True, elapsed)
    except Exception as e:
        return (False, str(e))

def load_test(max_workers=10, total_requests=50):
    top_stories = get_top_stories()
    if not top_stories:
        print("No top stories to test")
        return

    # Limit the number of requests to available top stories.
    requests_to_run = min(total_requests, len(top_stories))

    successes = 0
    failures = 0
    response_times = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # submit parallel threads to the executor to call `get_top_story_and_its_comment`.
        futures = [executor.submit(get_top_story_and_its_comment, top_stories[i % len(top_stories)])
                   for i in range(requests_to_run)]

        # returns future ordered by their completion.
        for future in as_completed(futures):
            success, data = future.result()
            if success:
                successes += 1
                response_times.append(data)
            else:
                failures += 1
                print(f"Request failed: |{data}|")

    print(f"Load Test with |{max_workers}| workers and |{total_requests}| requests")
    print(f"Successes: |{successes}|, Failures: |{failures}|")

    if response_times:
        print(f"Avg response time: |{sum(response_times)/len(response_times):.4f}| sec")
        print(f"Max response time: |{max(response_times):.4f}| sec")

if __name__ == "__main__":
    # Example run: increase max_workers gradually to find performance threshold.
    for workers in [5, 10, 20, 50]:
        load_test(max_workers=workers, total_requests=100)
