# coding: utf-8
import requests
from bs4 import BeautifulSoup
from xml_list import xmls
from PrettyPrint import prettyPrint

input_username = '2015118130'

headers = {

    'preDo': {
        'Host': '219.245.18.61',
        'Content-Type': 'text/xml; charset=utf-8',
        'Content-Length': 'length',
        'SOAPAction': "http://murpcn.com/murpwebservice/loginverifystudent_B",
    },

    'getAllGrade': {
        'Host': '219.245.18.61',
        'Content-Type': 'text/xml; charset=utf-8',
        'Content-Length': 'length',
        'SOAPAction': 'http://murpcn.com/murpwebservice/GetMyGrades',
    },

    'getTermGrage': {
        'Host': '219.245.18.61',
        'Content-Type': 'text/xml; charset=utf-8',
        'Content-Length': 'length',
        'SOAPAction': 'http://murpcn.com/murpwebservice/Mark',
    },
}

urls = {
    'preDo': 'http://219.245.18.61:81/MURPWebService/MURPMainService.asmx',
    'getAllGrade' : 'http://219.245.18.61:81/KEY/MURPNewsService.asmx',
    'getTermGrage' : 'http://219.245.18.61:81/KEY/MURPNewsService.asmx',
}


def Query(input_username, type):
    xml = xmls['preDo'].replace('2015118140', input_username)
    # 向接口发出带有xml的post请求
    response = requests.post(urls['preDo'], headers=headers['preDo'], data=xml)
    # 用bs解析响应文本
    soup = BeautifulSoup(response.text, 'lxml')
    # 得到关键信息

    try:
        _key = soup.umcid.string
    except:
        return 'ERROR'
    # 第二步再进行查询
    querystring = ''
    if type == 2:
        querystring = 'getAllGrade'
    elif type == 1:
        querystring = 'getTermGrage'

    xml = xmls[querystring].replace('80213', _key)
    response = requests.post(urls[querystring], headers=headers[querystring], data=xml)

    querylist = prettyPrint(BeautifulSoup(response.text, 'lxml'), type=querystring)

    return querylist


# if __name__ == '__main__':
#
#     # 第一步先查出关键信息
#     input_username = input('学号:')
#     xml = xmls['preDo'].replace('2015118140', input_username)
#     # 向接口发出带有xml的post请求
#     response = requests.post(urls['preDo'], headers=headers['preDo'], data=xml)
#     # 用bs解析响应文本
#     soup = BeautifulSoup(response.text, 'lxml')
#     # 得到关键信息
#     try:
#         _key = soup.umcid.string
#     except:
#         print('输入有误')
#         exit()
#
#     # 第二步再进行查询
#     p = input('1.历史成绩 2.学期成绩：')
#     querystring = ''
#     if p == '1':
#         querystring = 'getAllGrade'
#     elif p == '2':
#         querystring = 'getTermGrage'
#
#     xml = xmls[querystring].replace('80213', _key)
#     response = requests.post(urls[querystring], headers=headers[querystring], data=xml)
#     prettyPrint(BeautifulSoup(response.text, 'lxml'), type=querystring)
#
#     stop = input()