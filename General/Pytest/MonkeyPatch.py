# Common Syntax and Usage with Examples for monkeypatch

# 1. Replacing (patching) an attribute or method
import math

def test_monkeypatch_sqrt(monkeypatch):
    # Patch math.sqrt to always return 42
    monkeypatch.setattr(math, "sqrt", lambda x: 42)
    assert math.sqrt(25) == 42

# 2. Setting items in dictionaries
def test_monkeypatch_dict(monkeypatch):
    sample_dict = {"a": "original"}
    monkeypatch.setitem(sample_dict, "a", "patched")
    assert sample_dict["a"] == "patched"

# 3. Modifying environment variables
import os

def test_monkeypatch_env(monkeypatch):
    monkeypatch.setenv("MY_VARIABLE", "test_value")
    assert os.environ["MY_VARIABLE"] == "test_value"

# 4. Deleting attributes or environment variables
def test_monkeypatch_delattr(monkeypatch):
    class Dummy:
        value = "present"
    monkeypatch.delattr(Dummy, "value")
    assert not hasattr(Dummy, "value")

def test_monkeypatch_delenv(monkeypatch):
    os.environ["FOO"] = "1"
    monkeypatch.delenv("FOO")
    assert "FOO" not in os.environ