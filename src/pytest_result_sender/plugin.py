"""
@Filename:pytest-result-sender
@Author:  Freya
@Time:    2025/3/10 15:14
@Describe:...
"""

from datetime import datetime

# 导入pytest，收集用例
import pytest
import requests

data = {"passed": 0, "failed": 0}


def pytest_collection_finish(session: pytest.Session):
    # 用例加载完成之后执行，包含了全部用例
    data["total"] = len(session.items)
    print("==================:", data["total"])


def pytest_runtest_logreport(report: pytest.TestReport):
    if report.when == "call":
        data[report.outcome] += 1


def pytest_configure():
    """
    配置加载完毕之后
    测试用例执行之前
    """
    data["start_time"] = datetime.now()
    print(f"{datetime.now()} pytest开始执行")


def pytest_unconfigure():
    """
    测试用例执行之后
    """
    data["end_time"] = datetime.now()
    print(f"{datetime.now()} pytest结束执行")
    data["duration"] = data["end_time"] - data["start_time"]
    data["passed_ratio"] = f"{data['passed']/data['total']*100:.2f}%"

    """assert timedelta(seconds=3) > data["duration"] >= timedelta(seconds=2.5)
    assert data["total"] == 3
    assert data['passed']==2
    assert data['failed']==1
    assert data['passed_ratio']==f"{2/3*100:.2f}%"""

    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3be939f8-efad-42cb-ae49-af2d0e55b412"
    content = f"""
    python自动化测试结果


    测试时间：{data['start_time']}
    用例数量：{data['total']}
    执行时长：{data['duration']}
    测试通过：<font color="green">{data['passed']}</font>
    测试失败：<font color="red">{data['failed']}</font>
    测试通过率：{data['passed_ratio']}


    测试报告地址：http://baidu.com
    """
    requests.post(
        url,
        json={
            "msgtype": "markdown",
            "markdown": {
                "content": content,
            },
        },
    )
