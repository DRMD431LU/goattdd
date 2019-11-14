from django.urls import resolve
from django.test import TestCase
from .views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		request.method = 'GET'
		response = home_page(request)

		expected_html = render_to_string('home.html')
		
		self.assertEqual(response.content.decode(), expected_html)
		
		#self.assertTrue(response.content.startswith(b'<html>'))
		#self.assertIn(b'<title>To-Do lists</title>', response.content)
		#self.assertTrue(response.content.strip().endswith(b'</html>'))
	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'
		
		response = home_page(request)
		
		self.assertIn('A new list item', response.content.decode())
		expected_html = render_to_string(
			'home.html',
			{'new_item_text': 'A new list item'}
			)
		#print( response.content.decode() )
		#print( expected_html )

		self.assertEqual(response.content.decode(), expected_html)
		