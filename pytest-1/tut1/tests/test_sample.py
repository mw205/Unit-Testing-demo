# In this test file, we have two test functions: 
# test_add_num and test_add_str. 
# These functions are used to test the add function defined in the sample module.

from tut1.myapp.sample import add


def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"
