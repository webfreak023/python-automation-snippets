import string
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool


def domain_validator(link):
    print(link)
    try:
        response = requests.get(link)
        if response:
            if 'Download and Watch Latest' in str(response.content):
                with open('active_links.txt', 'a') as fileObj:
                    fileObj.write(link+'\n')
            else:
                with open('existing_links.json', 'a') as fileObj:
                    fileObj.write(str([{'link': link, 'exists': 'true'}]))
    except Exception as error:
        pass


def form_links():
    links = ['http://tamilrockers.%s%s' % (first_alpha, second_alpha) for first_alpha in string.ascii_lowercase[2:]
             for second_alpha in string.ascii_lowercase]
    for i in links:
        domain_validator(i)
    # threads = Pool(30)
    # list_of_active_links = threads.map(domain_validator, links)
    # threads.join()
    # threads.close()
    # print(list_of_active_links)


if __name__ == '__main__':
    form_links()
