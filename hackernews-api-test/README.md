# HackerNews API Acceptance Tests.

## Setup
- Install Python 3.9+.
- Run `pip install -e .` ONE TIME. This enables imports of packages without use of `src` in the imports.
- Install dependencies: `pip install -r requirements.txt`.

## Run Functional Tests
### Option1: Run From Terminal.
- navigate to the `hackernews-api-test` directory and use commands below to run specific tests.
- All tests (functional + performance)
  - `pytest` to run all tests.
  - `pytest -m <markername>` # see `pytest.ini` for all registered markers.
    - `pytest -m top_stories` to run all top stories tests.
- Pytest flags that can be used with any of the command above.
  - See `pytest.ini` -> `addopts` for default pytest flags set for this project.
  - See https://docs.pytest.org/en/6.2.x/usage.html for more details.
- Sample terminal output for `top stories` tests for command `pytest -m top_stories`.
```
===== test session starts =====
platform darwin -- Python 3.14.0, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/rumit311/PythonPracticeLocal/hackernews-api-test
configfile: pytest.ini
collected 13 items / 11 deselected / 2 selected                                                                                                                                         

src/tests/functional/test_top_stories.py::TestTopStories::test_happy_path 
----- live log setup -----
2025-11-22 23:30:02 [INFO] sending request to |https://hacker-news.firebaseio.com/v0/topstories.json| with data: |None|.
2025-11-22 23:30:03 [INFO] received response |<Response [200]>|.
PASSED                                                                                                                                                                            [ 50%]
src/tests/functional/test_top_stories.py::TestTopStories::test_empty_response 
----- live log call -----
2025-11-22 23:30:03 [INFO] Mock Response |{}|
PASSED                                                                                                                                                                            [100%]

===== 2 passed, 11 deselected in 0.89s =====
```

### Option2: Run From PyCharm IDE.
- **Option 2a**:
  - Go to the test file e.g. `test_items.py`.
  - Click the `Run` button (Green Triangle) from the top bar.
- **Option 2b**:
  - Go project explorer window.
  - right-click on the test file (e.g. `test_items.py`) or test package (e.g. `functioanl`).
  - Select Run `Python tests in fun...` option.

## Other Included Tests In The Project.
- A load test that can help measure the response time with increasing load.
- An example of all functional tests in a single module.

## Notes.
- The code in this package was tested with Python 3.14 and pytest-8.4.2 on Macbook Pro 2017 + Intel Core 5.
- Tests require internet access.
- The HackerNewsAPI used in this project is a public API which does not need any authentication or authorization. 
  - API downtime or rate limits may affect test results.
