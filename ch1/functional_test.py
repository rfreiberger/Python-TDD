
from selenium import webdriver

browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
browser.get('http://yahoo.com')
# assert 'Django' in browser.title
assert 'Yahoo' in browser.title
