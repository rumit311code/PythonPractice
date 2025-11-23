from setuptools import setup, find_packages

setup(
    name="hackernews_api_tests",
    version="1.0",
    author="Rumit Patel",
    description="Acceptance tests for HackerNews API",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "pytest"
    ],
)