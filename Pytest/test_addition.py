# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:39:04 2018

@author: admin
"""
import pytest

from addition import add, add_with_exception

def test_simple_add():
    assert add(1, 2) == 3
    assert add(1, 1) == 2
    assert add(105, 321) == 426

def test_invalid_add():
    assert add(-5, 5) is None

def test_invalid_add_exception():
    with pytest.raises(ValueError):
        assert add_with_exception(-5, 5)