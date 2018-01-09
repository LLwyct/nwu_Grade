# coding: utf-8
import requests
from bs4 import BeautifulSoup
from PrettyPrint import prettyPrint


xmls = {

    'preDo': '''<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                  <soap:Body>
                    <loginverifystudent_B xmlns="http://murpcn.com/murpwebservice/">
                      <loginname>2015118140</loginname>
                      <loginpass>2015118140</loginpass>
                      <tec>string</tec>
                      <logininfo>string</logininfo>
                      <strbak>string</strbak>
                    </loginverifystudent_B>
                  </soap:Body>
                </soap:Envelope>
                ''',

    'getAllGrade': '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetMyGrades xmlns="http://murpcn.com/murpwebservice/"><umcid>80213</umcid></GetMyGrades></soap:Body></soap:Envelope>',

    'getTermGrage': '''<?xml version="1.0" encoding="utf-8"?>
                        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                          <soap:Body>
                            <Mark xmlns="http://murpcn.com/murpwebservice/">
                              <umcid>80213</umcid>
                            </Mark>
                          </soap:Body>
                        </soap:Envelope>
                        ''',
}

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
    try:
        response = requests.post(urls['preDo'], headers=headers['preDo'], data=xml, timeout=3)
        # 用bs解析响应文本
        soup = BeautifulSoup(response.text, 'lxml')
    except:
        return 'ERROR'
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
    if querystring == '':
        return 'ERROR'
    xml = xmls[querystring].replace('80213', _key)
    try:
        response = requests.post(urls[querystring], headers=headers[querystring], data=xml, timeout=60)
        querylist = prettyPrint(BeautifulSoup(response.text, 'lxml'), type=querystring)
    except:
        return 'ERROR'
    # 返回最终结果
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
