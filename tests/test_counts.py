import pytest
import example_package
import example_package.internal_counts

def test_add_one():
    assert example_package.counts.add_one(1)==2

def test_add_two():
    assert example_package.internal_counts.add_two(1)==3
