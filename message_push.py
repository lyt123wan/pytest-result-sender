"""
@Filename:pytest-result-sender
@Author:  Freya
@Time:    2025/3/13 13:29
@Describe:...
"""

import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3be939f8-efad-42cb-ae49-af2d0e55b412"
content = """
python自动化测试结果


测试时间：<br/>
用例数量：<br/>
执行时长：<br/>
测试通过：<font color="green"></font><br/>
测试失败：<font color="red">1</font><br/>
测试通过率：<br/>


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
