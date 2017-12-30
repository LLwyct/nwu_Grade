import requests
from bs4 import BeautifulSoup
from xml_a import XML as XML_a
from xml_b import XML as XML_b
from PrettyPrint import prettyPrint

input_username = '2015118130'
input_password = '2015118130'

if __name__ == '__main__':

    input_username = input('学号:')

    input_password = input_username

    XML_a = XML_a.replace('2015118140', input_username)
    XML_a = XML_a.replace('2015118140', input_password)

    url_a = 'http://219.245.18.61:81/MURPWebService/MURPMainService.asmx'


    # 第一次查询
    header_a = {
                'Host': '219.245.18.61',
                'Content-Type': 'text/xml; charset=utf-8',
                'Content-Length': 'length',
                'SOAPAction': "http://murpcn.com/murpwebservice/loginverifystudent_B",
    }

    response = requests.post(url_a, headers=header_a, data=XML_a)
    soup = BeautifulSoup(response.text, 'lxml')
    _key = soup.umcid.string

    # 第二次查询
    XML_b = XML_b.replace('80213', _key)

    url_b = 'http://219.245.18.61:81/KEY/MURPNewsService.asmx'

    header_b = {
                'Host': '219.245.18.61',
                'Content-Type': 'text/xml; charset=utf-8',
                'Content-Length': 'length',
                'SOAPAction': 'http://murpcn.com/murpwebservice/GetMyGrades',
    }

    response = requests.post(url_b, headers=header_b, data=XML_b)
    soup = BeautifulSoup(response.text, 'lxml')
    prettyPrint(soup)
    stop = input()