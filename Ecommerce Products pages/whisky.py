from bs4 import BeautifulSoup
import requests
import pandas as pd



def Extract(page):
    base_url="https://www.thewhiskyexchange.com"
    url=f"https://www.thewhiskyexchange.com/c/503/beer?pg={page}&psize=24&sort=pasc"
    response=requests.get(url).text
    soup=BeautifulSoup(response,'html.parser')
    beers=soup.find_all('li', class_="product-grid__item")
    products_links=[]
    for i in beers:
        links=base_url+i.a['href']
        products_links.append(links)

    for i in products_links:
        response=requests.get(i).text
        soup=BeautifulSoup(response,'html.parser')
        beers_details={
        'Name':soup.find('h1', class_="product-main__name").text.strip(),
        'Price':soup.find('p', class_="product-action__price").text.strip(),
        'Desription':soup.find('div', class_="product-main__description").text.strip(),
        'Link':i
        }
        products.append(beers_details)
    return

if __name__=="__main__":
    while True:
        try:
            page=int(input('Enter page no that you want extract info: '))
            print(f'Filtering out info from all {page} pages....')
            print("")
            products=[]
            for i in range(1,page+1):
                Extract(i)
            df=pd.DataFrame(products)
            df.to_excel('files/whisky.xlsx', index=False)
            print('File saved Successfull')
        except Exception as ex:
            print(ex)
        break