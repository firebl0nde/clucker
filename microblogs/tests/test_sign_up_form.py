from django.test import TestCase
from django import forms
from microblogs.forms import SignUpForm
from microblogs.models import User

class UserModelTestCase(TestCase):
    
    def setUp(self):
        self.form_input = {
                'first_name'  : 'Jane',
                'last_name'   : 'Doe',
                'username'    : '@janedoe',
                'email'       : 'janedoe@example.org',
                'bio'         : ' This is my sweet bio.',
                'new_password': 'Pass12345rty',
                'password_confirmation' : 'Pass12345rty'
                }

    # form accepts valid input data 
    def test_valid_sign_up_form(self):
        form = SignUpForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    # form has the necessary fields
    def test_form_has_necessary_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, forms.EmailField))
        self.assertIn('bio', form.fields)
        self.assertIn('new_password', form.fields)
        new_password_widget  = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        password_confirmation_widget  = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(password_confirmation_widget, forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)

    #form user model validation 
    def test_user_model_validation(self):
        self.form_input['username'] = 'badusername'
        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())


    # new pass has correct format 
    def test_pass_must_contain_uppercase_char(self):
        self.form_input['new_password'] = 'password123'
        self.form_input['password_confirmation'] = 'password123'

        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())


    def test_pass_must_contain_lowercase_char(self):
        self.form_input['new_password'] = 'PASSWORD123'
        self.form_input['password_confirmation'] = 'PASSWORD123'

        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def test_pass_must_contain_number(self):
        self.form_input['new_password'] = 'passwordABS'
        self.form_input['password_confirmation'] = 'passwordABS'

        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())


    # new pass and password match
    def test_pass_and_confirmation_should_match(self):
        self.form_input['password_confirmation'] = 'WrongPassword123'

        form = SignUpForm(data = self.form_input)
        self.assertFalse(form.is_valid())





























