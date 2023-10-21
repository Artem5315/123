from urllib.parse import urlparse

urls = [
    'http://www.mail.ru/1.html',
    'https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie',
    'https://pythonru.com/uroki/biblioteka-pygame-chast-2-rabota-so-sprajtami',
    'https://news.mail.ru/politics/51550058/?frommail=1',
    'news.mail.ru/society/51554979/?frommail=1'
]

unique_urls = {}

for url in urls:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain not in unique_urls:
        unique_urls[domain] = url

result = list(unique_urls.values())
print(result)
