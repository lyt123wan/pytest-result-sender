"""
@Filename:pytest-result-sender
@Author:  Freya
@Time:    2025/3/12 17:18
@Describe:...
"""

import time


def test_api():
    time.sleep(2.1)  # 正常情况下2.5s后结束


def test_pass(): ...


def test_fail():
    assert False
