'''Написать программу, которая выведет на экран значения ключей. Задан следующий URL
адрес https://www.google.com/search?ei=qw3eqwe12e1w&amp;q=URL после
'''
from urllib.parse import urlparse, parse_qs

url = 'https://www.google.com/search?ei=qw3eqwe12e1w&q=URL'
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

for key, value in query_params.items():
    print(key, value)
