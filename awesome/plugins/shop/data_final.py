# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:02:57 2019

@author: 魏
"""

import re
from bs4 import BeautifulSoup
import requests as req

async def get_the_final(result: str) -> str:
    #获得五个回答
    global msg
    msg = ''
    r_res = re.compile('(\d)\s+(\d)\s+(\d)\s+(\d)\s+(\d+)\W+(\d+)')
    m_res = re.match(r_res,result)
    a1 = m_res.group(1)
    a2 = m_res.group(2)
    a3 = m_res.group(3)
    a4 = m_res.group(4)
    minm = m_res.group(5)
    maxm = m_res.group(6)
    
    td = re.compile('<td.*?>(.*?)</td>')
    url = 'https://www.yuque.com/api/v2/repos/385391/docs/2185141'
    url_head = {'User-Agent':'Mozilla/5.0','content-type':'application/json','X-Auth-Token':'kxiqyyLD2dtRROObtRL50IgswgWW07cBEK8uvP2R'}
    r = req.get(url,headers = url_head)
    r_content = BeautifulSoup(r.text,'html.parser')
    r_content_table = r_content.find_all('tr')
    #print(r_content_table)
    #创建分数统计列表
    goal=['']
    #创建+-统计
    list1=['']
    list2=['']
    #计数
    num = 1
    for e_tr in r_content_table[1:]:
        #初始化三个表
        goal.append('')
        list1.append('')
        list2.append('')
        
        s_e_tr = str(e_tr)
        r_td = re.findall(td,s_e_tr)
        mingcheng = r_td[1].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')
        chuliqi = r_td[2].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')
        pseyu = r_td[3].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')

        neichunsj = r_td[6].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')
        neichun = r_td[7].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')
        seyu = r_td[8].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')
        shoujia = r_td[9].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')
        yongtu = r_td[11].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')
        pinmu = r_td[12].replace('\\n','').replace('<p>','').replace('</p>','').replace('<br/>','')
        
        if neichunsj != '0':
            if a1 != '1':
                list1[num] = list1[num]+'+'
            if a3 == '1':
                list1[num] = list1[num]+'+'
        if neichun == '16':
            if a1 == '1':
                list2[num] = list2[num]+'-'
            if a1 == '3' or a1 == '4':
                list1[num] = list1[num]+'+'
            if a3 != '1':
                list1[num] = list1[num]+'+'
        if seyu == '0':
            if a3 == '1':
                list2[num] += '-'
        if yongtu == '3':
            if a1 == '1':
                list2[num] += '-'
            if a2 == '1':
                list2[num] += '-'
            if a2 == '3':
                list2[num] += '+'
        if pinmu == '1' or pinmu =='2':
            if a1 == '3':
                list1[num] += '+'
            if a3 != '1':
                list1[num] += '+'
            
    
        if len(list1[num]) > 0:
            if len(list1[num]) > len(list2[num]):
                if int(minm) < int(shoujia) and int(shoujia) < int(maxm):
                    msg += '\n'+'本款推荐：'+mingcheng
                    msg += '\n'+'处理器配置：'+chuliqi
                    msg += '\n'+'色域：'+pseyu
                    msg += '\n'+'售价：'+shoujia+'\n'
                    goal[num] = list1[num]
            if len(list1[num]) == 1 and len(list2[num]) > 1:
                msg += '\n'+'本款推荐：'+mingcheng
                msg += '\n'+'处理器配置：'+chuliqi
                msg += '\n'+'色域：'+pseyu
                msg += '\n'+'售价：'+shoujia+'\n'
        else:
            goal[num]=''
        num += 1
    try:
        return f'{msg}'
    except:
        return f'没有找到匹配的型号，尝试改变需求试试吧'