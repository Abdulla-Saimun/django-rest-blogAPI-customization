from turtle import title
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpClass(cls):
        # create user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')  # type: ignore
        testuser1.save()

        # create a blog post
        test_post = Post.objects.create(
            author='testuser1', title='Blog title', body='body content'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'test')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'body content')
