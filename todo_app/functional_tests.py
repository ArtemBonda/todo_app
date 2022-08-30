from selenium import webdriver

browser = webdriver.Firefox()           # запустить окно браузера
browser.get('http://localhost:9000')    # на хосте

assert 'worked' in browser.title        # Проверка что в заголовке страницы есть слово worked
