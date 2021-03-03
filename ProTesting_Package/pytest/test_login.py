import pytest


def test_case1(login):
    print("test_case1,需要登录")

def test_case2(login):
    print("test_case2,不需要登录")

def test_case3(login):
    print("test_case3,需要登录")

if __name__ == '__main__':
    pytest.main(["-v","-s"])