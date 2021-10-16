from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User

class UserModelTestCase(TestCase):
    def setUp(self):
       self.user = User.objects.create_user (
            '@johndoe',
            first_name = 'John',
            last_name = 'Doe',
            email = 'johndoe@example.org',
            password = '123Password',
            bio = 'i love it'
        )

    def test_valid_user(self):
        self._assert_user_is_valid()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('user is invalid')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
             self.user.full_clean()

    def _create_second_user(self):
        user = User.objects.create_user (
            '@janedoe',
            first_name = 'Jane',
            last_name = 'Doe',
            email = 'janedoe@example.org',
            password = '123Pass123',
            bio = 'jane here, we love it'
        )
        return user

########

# Username Test

########
    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_can_be_30_char_long(self):
        self.user.username = '@' + 'x'* 29
        self._assert_user_is_valid()

    def test_username_cannot_be_over_30_char_long(self):
        self.user.username = '@' + 'x'* 30
        self._assert_user_is_invalid()

    def test_username_must_start_with_at(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_at_least_3aplha_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username = '@j0hndoe2'
        self._assert_user_is_valid()

    def test_username_must_contain_only_one_at(self):
        self.user.username = '@@johndoe'
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()

#########

# First Name tests

#########

    def test_first_name_has_to_be_unique(self):
        second_user = self._create_second_user()
        self.user.first_name = second_user.first_name
        self._assert_user_is_valid()

    def test_first_name_cannot_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()

    def test_first_name_can_be_50_char_long(self):
        self.user.first_name = 'x'* 50
        self._assert_user_is_valid()

    def test_first_name_cannot_be_over_50_char_long(self):
        self.user.first_name = 'x'* 51
        self._assert_user_is_invalid()

 #########

 # Last Name Tests

 #########

    def test_last_name_has_to_be_unique(self):
        second_user = self._create_second_user()
        self.user.last_name = second_user.last_name
        self._assert_user_is_valid()

    def test_last_name_cannot_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_last_name_can_be_50_char_long(self):
        self.user.last_name = 'x'* 50
        self._assert_user_is_valid()

    def test_last_name_cannot_be_over_50_char_long(self):
        self.user.last_name = 'x'* 51
        self._assert_user_is_invalid()

#########

# Email tests

#########

    def test_email_has_to_be_unique(self):
        second_user = self._create_second_user()
        self.user.email = second_user.email
        self._assert_user_is_invalid()

    def test_email_cannot_be_blank(self):
        self.user.email = ''
        self._assert_user_is_invalid()

    def test_email_must_contain_username(self):
        self.user.email = '@example.org'
        self._assert_user_is_invalid()

    def test_email_should_contain_at(self):
        self.user.email = 'johndoe.example.org'
        self._assert_user_is_invalid()

    def test_email_should_contain_domain_name(self):
        self.user.email = 'johndoe@.org'
        self._assert_user_is_invalid()

    def test_email_should_contain_domain(self):
        self.user.email = 'johndoe@example'
        self._assert_user_is_invalid()

    def test_email_may_contain_numbers(self):
        self.user.email = 'johndoe2@example.org'
        self._assert_user_is_valid()

    def test_email_must_contain_only_one_at(self):
        self.user.email = 'johndoe@@example.org'
        self._assert_user_is_invalid()

#############

# Bio Tests

#############


    def test_bio_may_be_blank(self):
        self.user.bio = ''
        self._assert_user_is_valid()

    def test_email_may_not_be_unique(self):
        second_user = self._create_second_user()
        self.user.bio = second_user.bio
        self._assert_user_is_valid()

    def test_bio_may_have_520_char(self):
        self.user.bio = 'x' * 520
        self._assert_user_is_valid()

    def test_bio_cannot_have__morethan_520_char(self):
        self.user.bio = 'x' * 521
        self._assert_user_is_invalid()














# Create your tests here.
