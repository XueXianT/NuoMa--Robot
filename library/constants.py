# -*- coding: utf-8 -*-
import os
import shutil

# Wukong main directory
APP_PATH = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)

LIB_PATH = os.path.join(APP_PATH, "library")
LOGS_PATH = os.path.join(APP_PATH, "logs")
PLUGIN_PATH = os.path.join(APP_PATH, "plugins")

CUSTOM_CONFIG_NAME = "config.yml"

CONFIG_PATH = os.path.join(APP_PATH, CUSTOM_CONFIG_NAME)
