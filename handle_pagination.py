import requests
from bs4 import BeautifulSoup

root = 'https://subslikescript.com'
website = f"{root}/movies_letter-A"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

#pagination handling
pagination=soup.find('ul',class_='pagination')
pages=pagination.find('li',class_='page-item')
last_page=pages[-2].text # gives last page number before arrow
links = []
for page in range(1,int(last_page)+1)[:2]: #slicing to limit pages for testing
    website = f"{root}/movies_letter-A?page={page}"
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')



    box = soup.find('article', class_='main-article')
    
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    # print(links)
    for link in links:
        try:
            print(link)
            result = requests.get(f"{root}/{link}")
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text(strip=True)
            transcript = box.find('div', class_='full-script').get_text(separator=' ')
            with open(f'{title}.txt', 'w', encoding='utf-8') as f:
                f.write(transcript)
        except:
            print("--------- Link Not Working ------")
            print(link)
