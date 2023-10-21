'''Написать программу, которая сохраняет изображение по адресу &#39;https://httpbin.org/image/jpeg&#39; в текущую папку.'''
import requests

url = 'https://httpbin.org/image/jpeg'
response = requests.get(url)

with open('image.jpg', 'wb') as f:
    f.write(response.content)
