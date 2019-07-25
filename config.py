# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:05:25 2019

@author: 魏
"""
import re

from nonebot.default_config import *

HOST = '127.0.0.1'
PORT = 8080

SUPERUSERS = {1020883511}
COMMAND_START = ['',re.compile(r'[/!]+')]