import requests
from bs4 import BeautifulSoup
import pandas as pd

def ExtractInfo(tech, palace, page):
    base_url="https://in.indeed.com"
    url=f'https://in.indeed.com/jobs?q={tech}&l={palace}&start={page}'
    response=requests.get(url).text
    soup=BeautifulSoup(response,'html.parser')
    all_jobs=soup.find_all('div',class_="jobsearch-SerpJobCard")
    for i in all_jobs:
        try:
            jobs={
            'Title':i.find('a', class_="jobtitle").text.strip(),
            'Company':i.find('span', class_="company").text.strip(),
            'Location':i.find('span', class_="location").text.strip(),
            'Salary':i.find('span', class_="salaryText").text.strip(),
            'Posted_date':i.find('span', class_="date").text.strip(),
            'Links':base_url+i.h2.a['href']
            }
            job_list.append(jobs)
        except:
            Title="None"
            
if __name__=="__main__":
    while True:
        tech=input('Enter skill: ')
        palace=input('Enter location: ')
        page=int(input('Enter total page that you want to get: '))
        print(f'getting info from all {page} pages...')
        job_list=[]
        for i in range(1,page+1):
            ExtractInfo(tech, palace, i)
        df=pd.DataFrame(job_list)
        df.to_excel('files/Indeed.xlsx', index=False)
        print('File saved Succesfully')
        break