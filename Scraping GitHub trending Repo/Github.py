import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint

base_url='https://github.com'
def TrendingRepo():
    url='https://github.com/trending'
    response=requests.get(url)
    
    if (response.status_code)!=200:
        print('Error Occured')
        return
    else:
        soup=BeautifulSoup(response.text,'html.parser')
        repos=soup.find_all('article', class_="Box-row")
        for i in repos:
            repo={
            'Link':base_url+i.h1.a['href'],
            'Name':i.h1.a['href'][1:]
            }
            trending_repo.append(repo)
        return
        
    


if __name__=="__main__":
    try:
        print("Started scraping")
        trending_repo=[]
        TrendingRepo()
#         pprint.pprint(trending_repo)
        df=pd.DataFrame(trending_repo)
        df.to_excel('Github.xlsx',index=False)
        print('Saved')
    except Exception as ex:
        print(ex)