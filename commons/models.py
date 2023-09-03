"""
@Filename:   commons/models
@Author:      北凡
@Time:        2023/1/13 21:18
@Describe:    声明yaml用例格式
"""

from dataclasses import dataclass, asdict

import yaml


@dataclass
class CaseInfo:
    """用例信息"""

    title: str
    request: dict
    extract: dict
    validate: dict

    def to_yaml(self) -> str:
        """序列化成yaml字符串"""

        yaml_str = yaml.dump(asdict(self))

        return yaml_str

    @classmethod
    def by_yaml(cls, yaml_str):
        """反序列化"""
        obj = cls(**yaml.safe_load(yaml_str))

        return obj


if __name__ == '__main__':
    with open(
            r"/Users/gengxiaomeng/Documents/study/api_framework_20230129/testcases/test_2_login.yaml",
            encoding="utf-8") as f:
        data = yaml.safe_load(f)
    print(data)
    case_info = CaseInfo(**data)

    s = case_info.to_yaml()  # 字符串
    # print(s)
    new_case_info = case_info.by_yaml(s)

    print(new_case_info)
