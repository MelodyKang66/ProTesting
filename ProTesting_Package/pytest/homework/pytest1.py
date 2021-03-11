# -*- coding:utf-8 -*-
# type hints
import pytest


class TestCalc:
    def test_add(self):
        a = 3
        b = 2
        assert a + b == 5

    def test_mod(self):
        a = 3
        b = 2
        assert a - b == 1

    def test_mul(self):
        a = 3
        b = 2
        assert a * b == 6

    def test_div(self):
        a = 3
        b = 2
        assert a % b == 1


if __name__ == '__main__':
    pytest.main(["-v", "-s"])
