from django.test import TestCase
from django.core.exceptions import ValidationError
from microblogs.models import Post
from microblogs.models import User

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                '@johndoe',
                first_name = 'John',
                last_name = 'Doe',
                email = 'johndoe@example.org',
                password = 'Password123',
                bio = 'Hi i am John',

                )
        self.post = Post.objects.create (
                author = self.user,
                text = 'this is John;s first post', 
            )

    def test_is_valid_post(self):
        self._assert_post_is_valid()

    def test_author_cannot_be_blank(self):
        self.post.author = None 
        self._assert_post_is_invalid()

    def _assert_post_is_valid(self):
        try:
            self.post.full_clean()
        except (ValidationError):
            self.fail('post is invalid')


    def _assert_post_is_invalid(self):
        with self.assertRaises(ValidationError):
             self.post.full_clean()
    

    def test_text_may_have_280_char(self):
        self.user.bio = 'x' * 280
        self._assert_post_is_valid()

    def test_text_cannot_have__morethan_280_char(self):
        self.post.text = 'x' * 281
        self._assert_post_is_invalid()
     

########

# Username Test

########

#########

# First Name tests

#########
 #########

 # Last Name Tests

 #########


#########











#
