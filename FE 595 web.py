import requests
import os
from bs4 import BeautifulSoup
import csv

'''
view the random company website, print to the console
'''
def view_random_company():
    url = "http://3.95.249.159:8000/random_company"
    response = requests.request("GET", url)
    print('================ Step 1 ========================')
    print(response.text)


'''
parse the html and get name and purpose
'''
def name_purpose(html):
    soup = BeautifulSoup(html, 'html.parser')
    soups = soup.find_all('li')
    for soup in soups:
        if 'Name' in soup.text:
            name = soup.text[soup.text.find('Name') + 6:]
        elif 'Purpose' in soup.text:
            purpose = soup.text[soup.text.find('Purpose') + 9:]
    return name, purpose

'''
download html files into 'data' file
extract name and purpose
'''
def download_data():
    lst = []
    print('================ Step 2 ========================')
    isExists = os.path.exists('data')
    if not isExists:
        os.makedirs('data')
    # repeat 50 times
    for i in range(50):
        # download
        url = "http://3.95.249.159:8000/random_company"
        response = requests.request("GET", url)
        txt = str(response.text)
        print('downloading into data/%d.html' % i)
        open('data/%d.html' % i, 'w').write(txt)
        # extract name and purpose
        name, purpose = name_purpose(txt)
        lst.append([name, purpose])
    return lst

'''
use the [name, purpose] list and write them into csv file
'''
def savedata(lst):
    print('================ Step 3 ========================')
    company = open('FE595Data1.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(company)

    csv_writer.writerow(['name', 'purpose'])
    for name, purpose in lst:
        csv_writer.writerow([name, purpose])
    company.close()

if __name__ == '__main__':
    view_random_company()
    lst = download_data()
    savedata(lst)