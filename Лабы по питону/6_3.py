'''Написать программу для открытия всех ссылок, приведенных в некотором файле, в
отдельных вкладках браузера.'''
import webbrowser

with open('links.txt', 'r') as f:
    links = f.readlines()

for link in links:
    webbrowser.get().open_new_tab(link.strip())
