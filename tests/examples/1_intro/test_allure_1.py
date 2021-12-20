import pytest
import time


def test_success():
    """this test succeeds"""
    time.sleep(1)
    assert True


def test_failure():
    """this test fails"""
    assert 1  # -> AssertionError


def test_failure2():
    """this test fails"""
    assert 0  # -> AssertionError


@pytest.mark.skip(reason="Broken")
def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')


def test_broken2():
    a = []
    assert a[1]
