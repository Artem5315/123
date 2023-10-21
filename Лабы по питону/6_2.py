'''Дан URL-адрес, вывести значения параметров запроса – p и q. Например, дан url = &#39;http://example.com/?q=abc&amp;p=123&#39; Выведем abc 123'''
from urllib.parse import urlparse, parse_qs

url = 'http://example.com/?q=abc&p=123'
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

q_value = query_params.get('q', [None])[0]
p_value = query_params.get('p', [None])[0]

print(q_value, p_value)
