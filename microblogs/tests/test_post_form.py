from django.test import TestCase
from django import forms
from microblogs.forms import PostForm
from django.contrib.auth.hashers import check_password

class PostFormTestCase(TestCase):
    
    def setUp(self):
        self.form_input = {
                'text'  : 'This is a dummie text',
                }

    # form accepts valid input data 
    def test_valid_post_form(self):
        form = PostForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    # form has the necessary fields
    def test_form_has_necessary_fields(self):
        form = PostForm()
        self.assertIn('text', form.fields)






























