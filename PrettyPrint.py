from bs4 import BeautifulSoup

def prettyPrint(soup, type):

    wait_to_print = soup.find_all('publicstruct')

    if type == 'getAllGrade':
        for item in wait_to_print:
            print('{: <20}, {: <20}, {: <20}\n'.format(item.extend2.string.replace("\n", "").strip(),
                                                        item.extend3.string.replace("\n", "").strip(),
                                                        item.extend4.string.replace("\n", "").strip()))
    elif type == 'getTermGrage':
        for item in wait_to_print:
            print('{: <20}, {: <20}\n'.format(item.extend1.string.replace("\n", "").strip(),
                                              item.extend2.string.replace("\n", "").strip()))