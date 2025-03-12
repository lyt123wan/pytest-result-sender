"""
@Filename:pytest-result-sender
@Author:  Freya
@Time:    2025/3/10 15:14
@Describe:...
"""
from datetime import datetime


def pytest_configure():
    """
    配置加载完毕之后
    测试用例执行之前
    """
    print(f"{datetime.now()} pytest开始执行")


def pytest_unconfigure():
    """
    测试用例执行之后
    """
    print(f"{datetime.now()} pytest结束执行")
