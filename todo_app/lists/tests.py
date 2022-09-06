from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePage(TestCase):
    '''Тест домашней страницы'''

    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представлении домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный HTML'''
        request = HttpRequest() # создаем объект HttpRequest
        response = home_page(request) # передаем его представлению home_page, которое дает отклик
        html = response.content.decode('utf8') # извлекаем содержимое .content отклика и вызываем .decode(), чтобы конвертировать их в символьную строку HTML
        self.assertTrue(html.startswith('<html>')) # нужно, чтобы она начиналась с тега <html>
        self.assertTrue('<title>To-Do lists</title>', html) #  хотим разместить тег <title> со словами «To-Do lists»
        self.assertTrue(html.endswith('</html>'))