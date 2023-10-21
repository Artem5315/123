from urllib.parse import urlparse

urls = [
    "//www.cwi.nl:80/%7Eguido/Python.html",
    "http://stackoverflow.com/search?q=question",
    "http://www.example.org/default.html?ct=32&amp;op=92&amp;item=98"
]

for url in urls:
    parsed_url = urlparse(url)
    new_netloc = "www.admin.ru"
    new_url = parsed_url._replace(netloc=new_netloc).geturl()
    print(new_url)
