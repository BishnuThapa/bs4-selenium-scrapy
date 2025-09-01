import requests
from bs4 import BeautifulSoup


website = "https://subslikescript.com/movie/Titanic-120338"
result = requests.get(website)
content=result.text
soup=BeautifulSoup(content,'lxml')
# print(soup.prettify())

#Inside Article tag with class main-article print h1 heading
box=soup.find('article',class_='main-article')
heading=box.find('h1').get_text()
# print(heading)

# transcript=soup.find('div',class_='full-script').get_text(strip=True,separator=' ')
transcript=soup.find('div',class_='full-script').get_text(separator=' ')
print(transcript)

#exporting data to text file
with open('titanic.txt','w',encoding='utf-8') as f:
    f.write(transcript)
