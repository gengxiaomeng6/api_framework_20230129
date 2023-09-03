"""
@Filename:   commons/cases
@Author:      北凡
@Time:        2023/1/13 21:38
@Describe:    动态生成用例
"""
from pathlib import Path

from commons.exchange import Exchange
from commons.files import YamlFile
from commons.models import CaseInfo
from commons.session import Session

session = Session()

# yaml用例存放目录
case_path = Path(r"/Users/gengxiaomeng/Documents/study/api_framework_20230129/testcases")
exchanger = Exchange(
    r'/Users/gengxiaomeng/Documents/study/api_framework_20230129/testcases/test_2_login.yaml')


class TestAPI:  # 一个可以被pytest识别的测试类
    ...

    @classmethod  # 类方法
    def find_yaml_case(cls):
        """
        寻找和加载yaml文件
        :return: 
        """

        yaml_path_list = case_path.glob("**/test_*.yaml")
        for yaml_path in yaml_path_list:
            print(yaml_path)
            file = YamlFile(yaml_path)  # 自动读取yaml文件
            case_info = CaseInfo(**file)  # 自动验证yaml格式
            case_func = cls.new_case(case_info)  # 从yaml格式转为pytest格式
            setattr(cls, f"{yaml_path.name}", case_func)  # 把pytest格式添加到类中

    @classmethod  # 类方法
    def new_case(cls, case_info: CaseInfo):
        def test_func(self):
            # 0. 变量替换
            new_case_info = exchanger.replace(case_info)
            # 1. 发送请求
            resp = session.request(**new_case_info.request)
            # 2. 保存变量（接口关联）
            for var_name, extract_info in new_case_info.extract.items():
                print(var_name, extract_info)
                exchanger.extract(resp, var_name, *extract_info)
            # 3. 断言

        return test_func


TestAPI.find_yaml_case()
