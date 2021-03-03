import pytest
#不带参数的fixture默认参数为scope=function
@pytest.fixture()
def login():
    print("这是个登录方法")