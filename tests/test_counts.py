import example_package
import pytest

def test_add_one():
    assert example_package.counts.add_one(1) == 2


def test_add_two():
    assert example_package.counts.add_two(1) == 3


def test_add_two_f():
    assert example_package.counts.add_two(1) != 4


if __name__ == "__main__":
    # assert pytest.main([f"{__file__}::{test_helloworld.__name__}"]) == 0
    test_add_one()