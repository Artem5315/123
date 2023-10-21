'''Скачать содержимое страницы
&#39;http://www.gutenberg.org/cache/epub/1112/pg1112.txt&#39;. Вывести длину скачанного сообщения. Организовать блочную загрузку файла посредством метода iter_content по 8 Кб. Вывести на экран первые 300 символов.'''
import requests

url = 'http://www.gutenberg.org/cache/epub/1112/pg1112.txt'
response = requests.get(url)

print(len(response.content))

response = requests.get(url, stream=True)
chunk_size = 8 * 1024 # 8 Кб
data = b''
for chunk in response.iter_content(chunk_size):
    data += chunk
    if len(data) >= 300:
        break

print(data[:300])
