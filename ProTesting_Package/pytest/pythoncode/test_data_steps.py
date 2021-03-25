import pytest
import yaml

from pythoncode.caculator import Caculator


# 解析测试数据文件：
def get_datas():
    with open("data.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']

    return [add_datas, add_ids]


# 解析测试步骤文件：
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if 'add' == step:
            result = calc.add(a, b)
        elif 'add1' == step:
            result = calc.add1(a, b)
        assert expect == result


class TestCal:
    def setup_class(self):
        print("计算开始")
        self.cal = Caculator()

    def teardown_class(self):
        print("计算结束")



    def test_add_steps(self):
        a = 1
        b = 2
        expect = 3
        steps("step.yml",self.cal,a,b,expect)



    # @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    # def test_add(self, a, b, expect):
    #     result = self.cal.add(a, b)
    #     assert round(result, 2) == expect


if __name__ == '__main__':
    pytest.main(["-v", "-s"])
