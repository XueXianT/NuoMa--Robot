import time


def getTime():
    """
    获取当前系统时间 YYYY-MM-DD
    :return:
    """

    return time.strftime("%Y-%m-%d", time.localtime(time.time()))
