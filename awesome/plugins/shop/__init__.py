# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 01:24:40 2019

@author: 魏
"""

import time
from nonebot import on_command,CommandSession
from data_final import get_the_final
@on_command('shop',aliases=('电脑推荐','买电脑'))
async def shop(session: CommandSession):
    with open('E:\\bot_data\\num.txt') as f:
            num = int(f.readline())
    if num == 0:
        await session.send('您好，这里是IT侠机器人选机助手，接下来请你根据问题回答符合条件的答案，你将会看到五个问题，请按照要求在输入框中编辑答案，每题之间的答案留一个空格，在看到“请回复”之前请勿发送，谢谢配合')
        time.sleep(5)
        await session.send('您的学院是：\n1.文学院，历史学院，哲学系 ，法学院，政府管理学院，社会学院 ，外国语学院 ，海外教育学院 ，信息管理学院 ，商学院，医学院\n2.数学系，物理学院，天文与空间科学学院，生命科学学院，化学化工学院，环境学院，大气科学学院，地球科学与工程学院，地理与海洋科学学院，现代工程与应用科学学院，工程管理学院，电子科学与工程学院\n3.匡亚明学院计科方向，人工智能学院，计算即科学与技术系，软件学院\n4.新闻传播学院，建筑与城市规划学院\n请编辑对应的数字，别忘记留空格哦')
        time.sleep(10)
        await session.send('相信你已经编辑好了，我们看下一题')
        time.sleep(2)
        await session.send('您的游戏需求是：\n1.无游戏需求/很弱游戏需求：黄金矿工、各种小型游戏\n2.弱游戏需求（LOL等，显卡需求低）\n3.强游戏需求（3A大作级别）\n请编辑对应的数字，别忘记留空格哦')
        time.sleep(7)
        await session.send('相信你已经编辑好了，我们看下一题')
        time.sleep(2)
        await session.send('您的设计需求是:\n1.无设计\n2.弱设计（偶尔玩玩Photoshop，Premiere，Ai等，弱兴趣）\n3.强设计（需要经常使用，社团宣传部、美工组主力选手，手绘、设计、摄影、剪辑等强兴趣）\n请编辑对应的数字，别忘记留空格哦')
        time.sleep(7)
        await session.send('相信你已经编辑好了，我们看下一题')
        time.sleep(2)
        await session.send('您的系统偏好是：\n1.不喜欢Windows\n2.不喜欢Mac OS\n3.无偏好\n请编辑对应的数字，别忘记留空格哦')
        time.sleep(7)
        await session.send('相信你已经编辑好了，我们看下一题')
        time.sleep(2)
        await session.send('请问您的最高预算是：\n请这样编辑：最低价格（数字）-最高价格（数字），谢谢配合')
        time.sleep(7)
        await session.send('相信你已经编辑好了,请回复！')
        with open('E:\\bot_data\\num.txt', 'w') as f:
            f.write('1')
    result = session.get('final',prompt='请输入你的答案')
    print(result)
    with open('E:\\bot_data\\num.txt', 'w') as f:
            f.write('0')
    await session.send('结果正在计算，请稍等哦')
    msgs = await get_the_final(result)
    await session.send(msgs)
    
    
@shop.args_parser
async def _(session: CommandSession):
    var = session.current_arg_text
    if var == 'sssssssss':
        session.state['final']=var