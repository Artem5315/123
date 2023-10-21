'''В9-10 https://s13.ru/ из ленты новостей вывести заголовок
новости, количество комментариев и
ссылку на страницу с подробностями'''
import requests
from bs4 import BeautifulSoup

url = 'https://s13.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

news_list = soup.find_all('div', class_='news-item')

for news in news_list[:5]:
    title = news.find('a', class_='news-title').text.strip()
    comments_count = news.find('span', class_='comments-count').text.strip()
    link = news.find('a', class_='news-title')['href']
    print(f'{title}\n{comments_count}\n{link}\n')
