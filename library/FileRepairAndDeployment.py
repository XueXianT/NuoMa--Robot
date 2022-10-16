import os
from library import constants


def int():
    """
    初始化文件部署
    如果logs文件夹 plugins文件夹 或者config.yml等文件未存在
    该方法会初始化生成并补录信息
    :return:
    """

    # 补全 logs文件夹
    if not (os.path.isdir(constants.LOGS_PATH)):
        os.makedirs(constants.LOGS_PATH)
    # 补全 plugins文件夹
    if not (os.path.isdir(constants.PLUGIN_PATH)):
        os.makedirs(constants.PLUGIN_PATH)
