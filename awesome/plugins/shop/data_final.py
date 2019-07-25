# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:02:57 2019

@author: 魏
"""

import re
import pandas as pd
import requests as req

async def get_the_final(result: str) -> str:
#def get_the_final(result: str) -> str:
    #获得五个回答
    global msg
    msg = ''
    r_res = re.compile('(\d)\s+(\d)\s+(\d)\s+(\d)\s+(\d+)\W+(\d+)')
    m_res = re.match(r_res,result)
    a1,a2,a3,a4,minm,maxm = m_res.groups()
    
    url = 'https://www.yuque.com/api/v2/repos/385391/docs/2185141'
    url_head = {'User-Agent':'Mozilla/5.0','content-type':'application/json','X-Auth-Token':'{token}'}
    r = req.get(url,headers = url_head)
    r_content = r.text.replace('\\"','"')
    #创建分数统计列表
    goal=['']
    #创建+-统计
    list1=['']
    list2=['']
    #计数
    num = 1
    pd_table = pd.read_html(r_content, encoding='utf-8', header=0)[0]
    PCindex = list(pd_table.index)

    for e_tr in PCindex:
        #初始化三个表
        goal.append('')
        list1.append('')
        list2.append('')
            
        if  pd_table.loc[e_tr,'内存升级'] != 0:
            if a1 != 1:
                list1[num] = list1[num]+'+'
            if a3 == 1:
                list1[num] = list1[num]+'+'
        if pd_table.loc[e_tr,'内存/G'] == 16:
            if a1 == 1:
                list2[num] = list2[num]+'-'
            if a1 == 3 or a1 == 4:
                list1[num] = list1[num]+'+'
            if a3 != 1:
                list1[num] = list1[num]+'+'
        if pd_table.loc[e_tr,'屏幕色域（数字为%）'] == 0:
            if a3 == 1:
                list2[num] += '-'
        if pd_table.loc[e_tr,'用途'] == 3:
            if a1 == 1:
                list2[num] += '-'
            if a2 == 1:
                list2[num] += '-'
            if a2 == 3:
                list2[num] += '+'
        if pd_table.loc[e_tr,'屏幕描述'] == 1 or pd_table.loc[e_tr,'屏幕描述'] == 2:
            if a1 == 3:
                list1[num] += '+'
            if a3 != 1:
                list1[num] += '+'
            
    
        if len(list1[num]) > 0:
            if len(list1[num]) > len(list2[num]):
                if int(minm) < int(pd_table.loc[e_tr,'参考售价/元']) and int(pd_table.loc[e_tr,'参考售价/元']) < int(maxm):
                    msg += '\n'+'本款推荐：%s' % pd_table.loc[e_tr,'产品型号']
                    msg += '\n'+'处理器配置：%s' % pd_table.loc[e_tr,'处理器']
                    msg += '\n'+'色域：%s' % pd_table.loc[e_tr,'屏幕色域（数字为%）']
                    msg += '\n'+'参考售价：%d' % pd_table.loc[e_tr,'参考售价/元'] +'\n'
                    goal[num] = list1[num]
            if len(list1[num]) == 1 and len(list2[num]) > 1:
                msg += '\n'+'本款推荐：%s' % pd_table.loc[e_tr,'产品型号']
                msg += '\n'+'处理器配置：%s' % pd_table.loc[e_tr,'处理器']
                msg += '\n'+'色域：%s' % pd_table.loc[e_tr,'屏幕色域（数字为%）']
                msg += '\n'+'参考售价：%d' % pd_table.loc[e_tr,'参考售价/元']+'\n'
        else:
            goal[num]=''
        num += 1
    try:
        return f'{msg}'
    except:
        return f'没有找到匹配的型号，尝试改变需求试试吧'
    
    
#print(get_the_final("1 1 1 1 4000-5000"))